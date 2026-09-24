from chessapi._core import AsyncBaseClient, BaseClient
from chessapi.lichess._endpoints import AsyncUsersEndpoint, UsersEndpoint

LICHESS_BASE_URL = "https://lichess.org"


class LichessClient(BaseClient):
    """Synchronous client for Lichess API."""

    BASE_URL = LICHESS_BASE_URL

    @property
    def users(self) -> UsersEndpoint:
        return UsersEndpoint(self)


class AsyncLichessClient(AsyncBaseClient):
    """Asynchronous client for Lichess API."""

    BASE_URL = LICHESS_BASE_URL

    @property
    def users(self) -> AsyncUsersEndpoint:
        return AsyncUsersEndpoint(self)
