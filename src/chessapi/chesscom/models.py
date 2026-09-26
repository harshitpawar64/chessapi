from typing import Any

import msgspec


class StreamingPlatform(msgspec.Struct, kw_only=True, frozen=True):
    type: str
    channel_url: str


class ChessComPlayer(msgspec.Struct, kw_only=True, frozen=True):
    avatar: str | None = None
    player_id: int
    api_url: str = msgspec.field(name="@id")
    url: str
    name: str | None = None
    username: str
    title: str | None = None
    followers: int
    country: str
    location: str | None = None
    last_online: int
    joined: int
    status: str
    is_streamer: bool
    twitch_url: str | None = None
    verified: bool
    league: str | None = None
    streaming_platforms: list[StreamingPlatform] = []


class ChessComPlayerStats(msgspec.Struct, kw_only=True, frozen=True):
    chess_daily: dict[str, Any] = {}
    chess960_daily: dict[str, Any] = {}
    chess_rapid: dict[str, Any] = {}
    chess_bullet: dict[str, Any] = {}
    chess_blitz: dict[str, Any] = {}
    fide: int | None = None
    tactics: dict[str, Any] = {}
    puzzle_rush: dict[str, Any] = {}


class ChessComCountry(msgspec.Struct, kw_only=True, frozen=True):
    api_url: str = msgspec.field(name="@id")
    code: str
    name: str
