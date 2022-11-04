import json
import logging as log
import re as regex
from typing import Dict
from urllib.parse import urlparse, parse_qs

from pydantic import ValidationError
from youtube_dl import YoutubeDL

import modelsDL
from modelsDL import Format


class ParserLink:
    """Simple parser YouTube links"""

    def __init__(self, original_link: str) -> None:
        self.original_link: str = original_link
        self.regex_pattern = regex.compile(r"https://youtu\.be/([{0-9A-z}\-_]*$)")

    @property
    def _regex_parse(self) -> str or None:
        try:
            return regex.search(self.regex_pattern, self.original_link).group(1)
        except IndexError:
            return None

    @property
    def _parser_urllib(self) -> str or None:
        parse_result = urlparse(self.original_link)
        query_dict = parse_qs(parse_result.query)

        return query_dict["v"][0] \
            if query_dict.keys() \
            else None

    @property
    def get(self) -> str or None:
        r = None
        u = self._parser_urllib
        return r if r else (u if u else None)


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
    def _select_videos(video_object: modelsDL.Model) -> list[Format]:
        array_formats = video_object.formats
        return [
            f for f in array_formats
            if (f.acodec != "none") & (type(f.fps) is int)
        ]

    @property
    def _build_response(self) -> dict:
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

    @property
    def get(self) -> dict:
        return self._build_response
