from typing import Any

import msgspec


class Profile(msgspec.Struct, rename="camel", kw_only=True, frozen=True):
    flag: str | None = None
    location: str | None = None
    bio: str | None = None
    real_name: str | None = None
    fide_rating: int | None = None
    uscf_rating: int | None = None
    ecf_rating: int | None = None
    rcf_rating: int | None = None
    cfc_rating: int | None = None
    dsb_rating: int | None = None
    links: str | None = None


class GameCount(msgspec.Struct, kw_only=True, frozen=True):
    all: int = 0
    rated: int = 0
    draw: int = 0
    loss: int = 0
    win: int = 0
    bookmark: int = 0
    playing: int = 0
    imported: int = msgspec.field(name="import", default=0)
    me: int = 0


class PlayTime(msgspec.Struct, kw_only=True, frozen=True):
    total: int = 0
    tv: int = 0


class LichessUser(msgspec.Struct, rename="camel", kw_only=True, frozen=True):
    id: str
    username: str
    disabled: bool = False
    perfs: dict[str, Any] = {}
    title: str | None = None
    flair: str | None = None
    tos_violation: bool = False
    patron: bool = False
    patron_color: int | None = None
    created_at: int | None = None
    profile: Profile | None = None
    seen_at: int | None = None
    play_time: PlayTime | None = None
    url: str | None = None
    verified: bool = False
    streaming: bool = False
    count: GameCount | None = None
    trophies: list[dict[str, Any]] = []
    fide_id: int | None = None
    streamer: dict[str, Any] = {}
