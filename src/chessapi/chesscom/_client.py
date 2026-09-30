from functools import cached_property

from chessapi._core import AsyncBaseClient, BaseClient
from chessapi.chesscom._endpoints import *

CHESSCOM_BASE_URL = "https://api.chess.com/pub"


class ChessComClient(BaseClient):
    """Synchronous client for Chess.com Published Data API."""

    BASE_URL = CHESSCOM_BASE_URL

    @cached_property
    def players(self) -> PlayersEndpoint:
        return PlayersEndpoint(self)

    @cached_property
    def countries(self) -> CountriesEndpoint:
        return CountriesEndpoint(self)

    @cached_property
    def puzzles(self) -> PuzzlesEndpoint:
        return PuzzlesEndpoint(self)


class AsyncChessComClient(AsyncBaseClient):
    """Asynchronous client for Chess.com Published Data API."""

    BASE_URL = CHESSCOM_BASE_URL

    @cached_property
    def players(self) -> AsyncPlayersEndpoint:
        return AsyncPlayersEndpoint(self)

    @cached_property
    def countries(self) -> AsyncCountriesEndpoint:
        return AsyncCountriesEndpoint(self)

    @cached_property
    def puzzles(self) -> AsyncPuzzlesEndpoint:
        return AsyncPuzzlesEndpoint(self)
