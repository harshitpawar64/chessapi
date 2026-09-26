from typing import Any

from chessapi._core import AsyncBaseEndpoint, BaseEndpoint
from chessapi.chesscom.models import ChessComCountry


class CountriesEndpoint(BaseEndpoint):
    """Synchronous country endpoints."""

    def get(self, country_code: str) -> ChessComCountry:
        return self._client.request(
            "GET", f"/country/{country_code}", response_model=ChessComCountry
        )

    def get_players(self, country_code: str) -> list[str]:
        data = self._client.request(
            "GET", f"/country/{country_code}/players", response_model=dict[str, Any]
        )

        return data.get("players", [])


class AsyncCountriesEndpoint(AsyncBaseEndpoint):
    """Asynchronous country endpoints."""

    async def get(self, country_code: str) -> ChessComCountry:
        return await self._client.request(
            "GET", f"/country/{country_code}", response_model=ChessComCountry
        )

    async def get_players(self, country_code: str) -> list[str]:
        data = await self._client.request(
            "GET", f"/country/{country_code}/players", response_model=dict[str, Any]
        )

        return data.get("players", [])
