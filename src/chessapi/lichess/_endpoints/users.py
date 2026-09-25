from chessapi._core import AsyncBaseEndpoint, BaseEndpoint
from chessapi.lichess.models import LichessUser, LichessUserStatus


class UsersEndpoint(BaseEndpoint):
    """Synchronous user endpoints."""

    def get(self, username: str) -> LichessUser:
        params = {"trophies": True, "profile": True, "rank": True, "fideId": True}
        return self._client.request(
            "GET", f"/api/user/{username}", params=params, response_model=LichessUser
        )

    def get_batch(self, usernames: list[str]) -> list[LichessUser]:
        if not usernames:
            return []

        if len(usernames) > 300:
            raise ValueError(
                f"Cannot fetch more than 300 users per batch request, got {len(usernames)}."
            )

        params = {"profile": True, "rank": True}
        return self._client.request(
            "POST",
            "/api/users",
            params=params,
            content=",".join(usernames),
            response_model=list[LichessUser],
        )

    def get_status(self, usernames: list[str]) -> list[LichessUserStatus]:
        if not usernames:
            return []

        if len(usernames) > 100:
            raise ValueError(
                f"Cannot fetch more than 100 users per status request, got {len(usernames)}."
            )

        params = {"ids": ",".join(usernames), "withSignal": True, "withGameMetas": True}

        return self._client.request(
            "GET",
            "/api/users/status",
            params=params,
            response_model=list[LichessUserStatus],
        )


class AsyncUsersEndpoint(AsyncBaseEndpoint):
    """Asynchronous user endpoints."""

    async def get(self, username: str) -> LichessUser:
        params = {"trophies": True, "profile": True, "rank": True, "fideId": True}
        return await self._client.request(
            "GET", f"/api/user/{username}", params=params, response_model=LichessUser
        )

    async def get_batch(self, usernames: list[str]) -> list[LichessUser]:
        if not usernames:
            return []

        if len(usernames) > 300:
            raise ValueError(
                f"Cannot fetch more than 300 users per batch request, got {len(usernames)}."
            )

        params = {"profile": True, "rank": True}
        return await self._client.request(
            "POST",
            "/api/users",
            params=params,
            content=",".join(usernames),
            response_model=list[LichessUser],
        )

    async def get_status(self, usernames: list[str]) -> list[LichessUserStatus]:
        if not usernames:
            return []

        if len(usernames) > 100:
            raise ValueError(
                f"Cannot fetch more than 100 users per status request, got {len(usernames)}."
            )

        params = {"ids": ",".join(usernames), "withSignal": True, "withGameMetas": True}

        return await self._client.request(
            "GET",
            "/api/users/status",
            params=params,
            response_model=list[LichessUserStatus],
        )
