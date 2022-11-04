from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Format(BaseModel):
    abr: Optional[float] = None
    acodec: str
    asr: Optional[int]
    container: Optional[str] = None
    ext: str
    filesize: Optional[int]
    format: str
    format_id: str
    format_note: str
    fps: Optional[int]
    height: Optional[int]
    protocol: str
    quality: int
    tbr: float
    url: str
    vcodec: str
    width: Optional[int]
    vbr: Optional[float] = None


class RequestedFormat(BaseModel):
    acodec: str
    asr: Optional[int]
    container: str
    ext: str
    filesize: int
    format: str
    format_id: str
    format_note: str
    fps: Optional[int]
    height: Optional[int]
    protocol: str
    quality: int
    url: str
    vbr: Optional[float] = None
    vcodec: str
    width: Optional[int]
    abr: Optional[float] = None


class EnItem(BaseModel):
    ext: str
    url: str


class Thumbnail(BaseModel):
    height: int
    id: str = None
    resolution: str
    url: str
    width: int


class Model(BaseModel):
    acodec: str
    average_rating: Any
    categories: List[str]
    channel: str
    channel_id: str
    channel_url: str
    description: str = None
    duration: int
    ext: str
    format: str = None
    format_id: str
    formats: List[Format]
    fps: int
    height: int
    id: str
    is_live: Any
    playlist: Any
    playlist_index: Any
    requested_formats: List[RequestedFormat]
    requested_subtitles: Any
    resolution: Any
    stretched_ratio: Any
    tags: List[str]
    thumbnail: str
    thumbnails: List[Thumbnail]
    title: str
    vcodec: str
    view_count: int
    width: int
