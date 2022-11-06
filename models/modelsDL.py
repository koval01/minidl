from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Format(BaseModel):
    abr: Optional[float] = None
    acodec: str = None
    asr: Optional[int]
    container: Optional[str] = None
    ext: str
    filesize: Optional[int] = None
    format: str
    format_id: str
    format_note: str = None
    fps: Optional[int]
    height: Optional[int]
    protocol: str
    quality: int = None
    tbr: float = None
    url: str
    vcodec: str = None
    width: Optional[int]
    vbr: Optional[float] = None


class RequestedFormat(BaseModel):
    acodec: str = None
    asr: Optional[int]
    container: str
    ext: str
    filesize: int = None
    format: str
    format_id: str
    fps: Optional[int]
    height: Optional[int]
    protocol: str
    quality: int = None
    url: str
    vbr: Optional[float] = None
    vcodec: str = None
    width: Optional[int]
    abr: Optional[float] = None


class EnItem(BaseModel):
    ext: str
    url: str


class Model(BaseModel):
    acodec: str = None
    channel: str = None
    channel_id: str = None
    channel_url: str = None
    description: str = None
    duration: int = None
    ext: str
    format: str = None
    format_id: str
    formats: List[Format] = None
    fps: int = None
    height: int = None
    id: str
    is_live: Any
    requested_formats: List[RequestedFormat] = None
    requested_subtitles: Any
    resolution: Any
    stretched_ratio: Any
    title: str
    vcodec: str = None
    view_count: int = None
    width: int = None
