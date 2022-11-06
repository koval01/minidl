import json
import logging as log
import re as regex
from typing import Dict, List

from pydantic import ValidationError
from youtube_dl import YoutubeDL

from models import modelsDL
from models.modelsDL import Format


class Video:
    """Get video with youtube-dl lib"""

    def __init__(self, url: str) -> None:
        self.url: str = url

    def _check_short(self) -> str:
        return "https://youtu.be/%s" % self.url.split("/")[-1:][0] \
            if "youtube.com/shorts/" in self.url else self.url

    def _youtube_playlist(self) -> str:
        pattern = regex.compile(r"list=[A-z\d\-_]*")
        return regex.sub(pattern, "", self.url) \
            if "youtube.com" in self.url else self.url

    @property
    def _get_dl(self) -> YoutubeDL or None:
        with YoutubeDL() as ydl:
            self.url = self._check_short()
            self.url = self._youtube_playlist()

            return ydl.extract_info(self.url, download=False)

    @staticmethod
    def _build_model(video_object: Dict) -> modelsDL.Model or list:
        try:
            return modelsDL.Model(**video_object)
        except ValidationError as e:
            return json.loads(e.json())

    @staticmethod
    def _select_videos(video_object: modelsDL.Model) -> List[Format]:
        array_formats = video_object.formats
        check_format = lambda format_var: len([
            ft for ft in [
                "x360", "x720",
                "360x", "720x",
                "360p", "720p"
            ]
            if ft in format_var]) != 0
        return [
            f for f in array_formats
            if check_format(f.format)
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
