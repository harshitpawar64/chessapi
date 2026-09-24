from chessapi._core import AsyncBaseEndpoint, BaseEndpoint
from chessapi.chesscom.models import ChessComPlayer


class PlayersEndpoint(BaseEndpoint):
    """Synchronous player endpoints."""

    def get(self, username: str) -> ChessComPlayer:
        """Fetch player profile by username."""
        return self._client.request(
            "GET", f"/player/{username}", response_model=ChessComPlayer
        )


class AsyncPlayersEndpoint(AsyncBaseEndpoint):
    """Asynchronous player endpoints."""

    async def get(self, username: str) -> ChessComPlayer:
        """Fetch player profile by username."""
        return await self._client.request(
            "GET", f"/player/{username}", response_model=ChessComPlayer
        )
