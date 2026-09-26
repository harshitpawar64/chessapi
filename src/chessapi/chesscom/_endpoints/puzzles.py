from chessapi._core import AsyncBaseEndpoint, BaseEndpoint
from chessapi.chesscom.models import ChessComPuzzle


class PuzzlesEndpoint(BaseEndpoint):
    """Synchronous puzzles endpoints."""

    def get_daily(self) -> ChessComPuzzle:
        return self._client.request("GET", "/puzzle", response_model=ChessComPuzzle)


class AsyncPuzzlesEndpoint(AsyncBaseEndpoint):
    """Asynchronous puzzles endpoints."""

    async def get_daily(self) -> ChessComPuzzle:
        return await self._client.request(
            "GET", "/puzzle", response_model=ChessComPuzzle
        )
