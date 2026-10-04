from functools import cached_property

from chessapi._core import AsyncBaseClient, BaseClient
from chessapi.lichess._endpoints import *

LICHESS_BASE_URL = "https://lichess.org"


class LichessClient(BaseClient):
    """Synchronous client for Lichess API."""

    BASE_URL = LICHESS_BASE_URL

    def __init__(
        self,
        token: str | None = None,
        *,
        headers: dict[str, str] | None = None,
        **kwargs,
    ):
        headers = (
            {"Authorization": f"Bearer {token}", **(headers or {})}
            if token
            else headers
        )
        super().__init__(headers=headers, **kwargs)

    @cached_property
    def users(self) -> UsersEndpoint:
        return UsersEndpoint(self)

    @cached_property
    def puzzles(self) -> PuzzlesEndpoint:
        return PuzzlesEndpoint(self)


class AsyncLichessClient(AsyncBaseClient):
    """Asynchronous client for Lichess API."""

    BASE_URL = LICHESS_BASE_URL

    def __init__(
        self,
        token: str | None = None,
        *,
        headers: dict[str, str] | None = None,
        **kwargs,
    ):
        headers = (
            {"Authorization": f"Bearer {token}", **(headers or {})}
            if token
            else headers
        )
        super().__init__(headers=headers, **kwargs)

    @cached_property
    def users(self) -> AsyncUsersEndpoint:
        return AsyncUsersEndpoint(self)

    @cached_property
    def puzzles(self) -> AsyncPuzzlesEndpoint:
        return AsyncPuzzlesEndpoint(self)
