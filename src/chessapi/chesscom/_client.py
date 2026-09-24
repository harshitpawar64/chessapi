from chessapi._core import AsyncBaseClient, BaseClient
from chessapi.chesscom._endpoints import AsyncPlayersEndpoint, PlayersEndpoint

CHESSCOM_BASE_URL = "https://api.chess.com/pub"


class ChessComClient(BaseClient):
    """Synchronous client for Chess.com Published Data API."""

    BASE_URL = CHESSCOM_BASE_URL

    @property
    def players(self) -> PlayersEndpoint:
        return PlayersEndpoint(self)


class AsyncChessComClient(AsyncBaseClient):
    """Asynchronous client for Chess.com Published Data API."""

    BASE_URL = CHESSCOM_BASE_URL

    @property
    def players(self) -> AsyncPlayersEndpoint:
        return AsyncPlayersEndpoint(self)
