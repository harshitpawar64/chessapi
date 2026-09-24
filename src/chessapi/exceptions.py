from typing import Any

import httpx


class ChessAPIError(Exception):
    """Base exception for all errors raised by chessapi."""


class NetworkError(ChessAPIError):
    """Raised when a network or connection error occurs (DNS failure, connection refused, offline)."""


class TimeoutError(ChessAPIError):
    """Raised when an API request times out."""


class DecodeError(ChessAPIError):
    """Raised when decoding a response fails (e.g. unexpected schema or corrupted payload)."""


class APIResponseError(ChessAPIError):
    """Base exception for HTTP errors returned by chess APIs."""

    def __init__(
        self,
        message: str,
        status_code: int,
        response: httpx.Response,
        details: Any | None = None,
    ) -> None:
        super().__init__(f"[{status_code}] {message}")
        self.message = message
        self.status_code = status_code
        self.response = response
        self.details = details


class BadRequestError(APIResponseError):
    """Raised on 400 Bad Request (malformed request or parameters)."""


class AuthenticationError(APIResponseError):
    """Raised on 401 Unauthorized (missing or invalid API token)."""


class PermissionDeniedError(APIResponseError):
    """Raised on 403 Forbidden (insufficient permissions or scopes)."""


class NotFoundError(APIResponseError):
    """Raised on 404 Not Found (requested resource does not exist)."""


class ResourceGoneError(APIResponseError):
    """Raised on 410 Gone (resource was permanently removed and will never return)."""


class RateLimitError(APIResponseError):
    """Raised on 429 Too Many Requests (rate limit exceeded)."""

    def __init__(
        self,
        message: str,
        status_code: int,
        response: httpx.Response,
        retry_after: float | None = None,
        details: Any | None = None,
    ) -> None:
        super().__init__(message, status_code, response, details)
        self.retry_after = retry_after


class ServerError(APIResponseError):
    """Raised on 5xx Server Errors (upstream server error or maintenance)."""
