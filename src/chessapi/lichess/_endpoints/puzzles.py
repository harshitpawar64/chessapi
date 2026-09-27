from chessapi._core import AsyncBaseEndpoint, BaseEndpoint
from chessapi.lichess.models import LichessPuzzle


class PuzzlesEndpoint(BaseEndpoint):
    """Synchronous puzzles endpoints."""

    def get(self, puzzle_id: str) -> LichessPuzzle:
        return self._client.request(
            "GET", f"/api/puzzle/{puzzle_id}", response_model=LichessPuzzle
        )


class AsyncPuzzlesEndpoint(AsyncBaseEndpoint):
    """Asynchronous puzzles endpoints."""

    async def get(self, puzzle_id: str) -> LichessPuzzle:
        return await self._client.request(
            "GET", f"/api/puzzle/{puzzle_id}", response_model=LichessPuzzle
        )
