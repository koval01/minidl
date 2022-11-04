import json
import logging as log
from typing import Dict, List
from urllib.parse import urlparse, parse_qs

from pydantic import ValidationError
from youtube_dl import YoutubeDL

from models import modelsDL
from models.modelsDL import Format


class ParserLink:
    """Simple parser YouTube links"""

    def __init__(self, original_link: str) -> None:
        self.original_link: str = original_link

    @property
    def _path_parse(self) -> str or None:
        try:
            index = 1
            if "/shorts/" in self.original_link:
                index += 1
            return urlparse(self.original_link).path.split("/")[index]
        except IndexError:
            return None

    @property
    def _query_parse(self) -> str or None:
        parse_result = urlparse(self.original_link)
        query_dict = parse_qs(parse_result.query)

        return query_dict["v"][0] \
            if query_dict.keys() \
            else None

    @property
    def get(self) -> str or None:
        p = self._path_parse
        q = self._query_parse
        return q if q else (p if p else None)


class Video:
    """Get video with youtube-dl lib"""

    def __init__(self, video_id: int) -> None:
        self.video_id: int = video_id

    @property
    def _get_dl(self) -> YoutubeDL or None:
        with YoutubeDL() as ydl:
            return ydl.extract_info(
                'https://www.youtube.com/watch?v=%s' % self.video_id,
                download=False
            )

    @staticmethod
    def _build_model(video_object: Dict) -> modelsDL.Model or list:
        try:
            return modelsDL.Model(**video_object)
        except ValidationError as e:
            return json.loads(e.json())

    @staticmethod
    def _select_videos(video_object: modelsDL.Model) -> List[Format]:
        array_formats = video_object.formats
        return [
            f for f in array_formats
            if (f.acodec != "none") & (type(f.fps) is int)
        ]

    @property
    def _build_response(self) -> dict:
        try:
            dl = self._get_dl
            response = self._build_model(dl)
            if type(response) is list:
                log.warning(response)
                return {}

            videos = self._select_videos(response)

            return {
                "duration": response.duration,
                "title": response.title,
                "url": videos[-1:][0].url
            }
        except Exception as e:
            log.warning(e)

    @property
    def get(self) -> dict:
        return self._build_response
