from chessapi._core import AsyncBaseEndpoint, BaseEndpoint
from chessapi.chesscom.models import ChessComPlayer, ChessComPlayerStats


class PlayersEndpoint(BaseEndpoint):
    """Synchronous player endpoints."""

    def get(self, username: str) -> ChessComPlayer:
        """Fetch player profile by username."""
        return self._client.request(
            "GET", f"/player/{username}", response_model=ChessComPlayer
        )

    def get_stats(self, username: str) -> ChessComPlayerStats:
        return self._client.request(
            "GET", f"/player/{username}/stats", response_model=ChessComPlayerStats
        )

    def get_titled(self, title: str) -> list[str]:
        data = self._client.request(
            "GET", f"/titled/{title}", response_model=dict[str, list[str]]
        )

        return data.get("players", [])


class AsyncPlayersEndpoint(AsyncBaseEndpoint):
    """Asynchronous player endpoints."""

    async def get(self, username: str) -> ChessComPlayer:
        """Fetch player profile by username."""
        return await self._client.request(
            "GET", f"/player/{username}", response_model=ChessComPlayer
        )

    async def get_stats(self, username: str) -> ChessComPlayerStats:
        return await self._client.request(
            "GET", f"/player/{username}/stats", response_model=ChessComPlayerStats
        )

    async def get_titled(self, title: str) -> list[str]:
        data = await self._client.request(
            "GET", f"/titled/{title}", response_model=dict[str, list[str]]
        )

        return data.get("players", [])
