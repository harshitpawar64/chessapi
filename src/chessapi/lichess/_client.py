from chessapi._core import AsyncBaseClient, BaseClient
from chessapi.lichess._endpoints import *

LICHESS_BASE_URL = "https://lichess.org"


class LichessClient(BaseClient):
    """Synchronous client for Lichess API."""

    BASE_URL = LICHESS_BASE_URL

    @property
    def users(self) -> UsersEndpoint:
        return UsersEndpoint(self)

    @property
    def puzzles(self) -> PuzzlesEndpoint:
        return PuzzlesEndpoint(self)


class AsyncLichessClient(AsyncBaseClient):
    """Asynchronous client for Lichess API."""

    BASE_URL = LICHESS_BASE_URL

    @property
    def users(self) -> AsyncUsersEndpoint:
        return AsyncUsersEndpoint(self)

    @property
    def puzzles(self) -> AsyncPuzzlesEndpoint:
        return AsyncPuzzlesEndpoint(self)
