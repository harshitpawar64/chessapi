from collections.abc import Mapping
from types import TracebackType
from typing import Any, ClassVar, Self, TypeVar, overload

import httpx
import msgspec

from chessapi import __version__
from chessapi.exceptions import (
    APIResponseError,
    AuthenticationError,
    BadRequestError,
    DecodeError,
    NetworkError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    ResourceGoneError,
    ServerError,
    TimeoutError,
)

DEFAULT_USER_AGENT = f"chessapi/{__version__}"

T = TypeVar("T")


def _handle_response_error(response: httpx.Response) -> None:
    if not response.is_error:
        return

    details: Any | None = None
    try:
        data = response.json()
        if isinstance(data, dict):
            details = data
            message = str(data.get("message") or data.get("error") or response.text)
        else:
            message = response.text
    except (ValueError, UnicodeDecodeError):
        message = response.text or response.reason_phrase or "Unknown API error"

    status = response.status_code

    if status == 400:
        raise BadRequestError(message, status, response, details)
    if status == 401:
        raise AuthenticationError(message, status, response, details)
    if status == 403:
        raise PermissionDeniedError(message, status, response, details)
    if status == 404:
        raise NotFoundError(message, status, response, details)
    if status == 410:
        raise ResourceGoneError(message, status, response, details)
    if status == 429:
        retry_after = None
        try:
            retry_after = float(response.headers.get("Retry-After"))
        except (ValueError, TypeError):
            pass
        raise RateLimitError(message, status, response, retry_after, details)
    if status >= 500:
        raise ServerError(message, status, response, details)

    raise APIResponseError(message, status, response, details)


def _decode_response(
    response: httpx.Response, response_model: type[T] | None
) -> T | httpx.Response:
    _handle_response_error(response)

    if response_model:
        try:
            return msgspec.json.decode(response.content, type=response_model)
        except msgspec.DecodeError as e:
            raise DecodeError(
                f"Failed to decode response into {response_model}: {e}"
            ) from e

    return response


class BaseClient:
    BASE_URL: ClassVar[str]

    def __init__(
        self,
        user_agent: str | None = None,
        headers: dict[str, str] | None = None,
        timeout: float = 10.0,
    ) -> None:
        headers = {"User-Agent": user_agent or DEFAULT_USER_AGENT, **(headers or {})}

        self._client = httpx.Client(
            base_url=self.BASE_URL,
            headers=headers,
            timeout=timeout,
            follow_redirects=True,
        )

    @overload
    def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        content: bytes | str | None = None,
        json: Any | None = None,
        response_model: type[T],
    ) -> T: ...

    @overload
    def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        content: bytes | str | None = None,
        json: Any | None = None,
        response_model: None = None,
    ) -> httpx.Response: ...

    def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        content: bytes | str | None = None,
        json: Any | None = None,
        response_model: type[T] | None = None,
    ) -> T | httpx.Response:
        try:
            response = self._client.request(
                method=method,
                url=endpoint,
                params=params,
                headers=headers,
                content=content,
                json=json,
            )
        except httpx.TimeoutException as e:
            raise TimeoutError(f"Request timed out: {e}") from e
        except httpx.RequestError as e:
            raise NetworkError(f"Network error while connecting to API: {e}") from e

        return _decode_response(response, response_model)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()


class AsyncBaseClient:
    BASE_URL: ClassVar[str]

    def __init__(
        self,
        user_agent: str | None = None,
        headers: dict[str, str] | None = None,
        timeout: float = 10.0,
    ) -> None:
        headers = {"User-Agent": user_agent or DEFAULT_USER_AGENT, **(headers or {})}
        self._client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers=headers,
            timeout=timeout,
            follow_redirects=True,
        )

    @overload
    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        content: bytes | str | None = None,
        json: Any | None = None,
        response_model: type[T],
    ) -> T: ...

    @overload
    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        content: bytes | str | None = None,
        json: Any | None = None,
        response_model: None = None,
    ) -> httpx.Response: ...

    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        content: bytes | str | None = None,
        json: Any | None = None,
        response_model: type[T] | None = None,
    ) -> T | httpx.Response:
        try:
            response = await self._client.request(
                method=method,
                url=endpoint,
                params=params,
                headers=headers,
                content=content,
                json=json,
            )
        except httpx.TimeoutException as e:
            raise TimeoutError(f"Request timed out: {e}") from e
        except httpx.RequestError as e:
            raise NetworkError(f"Network error while connecting to API: {e}") from e

        return _decode_response(response, response_model)

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.aclose()
