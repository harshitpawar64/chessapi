from chessapi._core import AsyncBaseEndpoint, BaseEndpoint
from chessapi.chesscom.models import ChessComCountry


class CountriesEndpoint(BaseEndpoint):
    """Synchronous country endpoints."""

    def get(self, country_code: str) -> ChessComCountry:
        return self._client.request(
            "GET", f"/country/{country_code}", response_model=ChessComCountry
        )


class AsyncCountriesEndpoint(AsyncBaseEndpoint):
    """Asynchronous country endpoints."""

    async def get(self, country_code: str) -> ChessComCountry:
        return await self._client.request(
            "GET", f"/country/{country_code}", response_model=ChessComCountry
        )
