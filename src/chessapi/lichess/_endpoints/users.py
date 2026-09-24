from chessapi._core import AsyncBaseEndpoint, BaseEndpoint
from chessapi.lichess.models import LichessUser


class UsersEndpoint(BaseEndpoint):
    """Synchronous user endpoints."""

    def get(self, username: str) -> LichessUser:
        params = {"trophies": True, "profile": True, "rank": True, "fideId": True}
        return self._client.request(
            "GET", f"/api/user/{username}", params=params, response_model=LichessUser
        )


class AsyncUsersEndpoint(AsyncBaseEndpoint):
    """Asynchronous user endpoints."""

    async def get(self, username: str) -> LichessUser:
        params = {"trophies": True, "profile": True, "rank": True, "fideId": True}
        return await self._client.request(
            "GET", f"/api/user/{username}", params=params, response_model=LichessUser
        )
