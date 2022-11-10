import json
import logging as log
import re as regex
from typing import Dict, List

from flask import request
from pydantic import ValidationError
from yt_dlp import YoutubeDL

import proxy
from models import modelsDL
from models.modelsDL import Format


class Video:
    """Get video with youtube-dl lib"""

    def __init__(self, secret_key: bytes, url: str) -> None:
        self.secret_key: bytes = secret_key
        self.url: str = url

        self.proxy_need_hosts = (
            "porntube.com",
            "instagram.com"
        )

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

    def _encrypt_link(self, source_url: str) -> str:
        for host in self.proxy_need_hosts:
            if host in source_url:
                return "%smedia_proxy/%s" % (
                    request.host_url,
                    proxy.Proxy(self.secret_key).encrypt_url(source_url)
                )

        return source_url

    @staticmethod
    def _build_model(video_object: Dict) -> modelsDL.Model or list:
        try:
            return modelsDL.Model(**video_object)
        except ValidationError as e:
            return json.loads(e.json())

    def _check_audio(self, format_object: modelsDL.Format) -> bool:
        if any(("youtube.com" in self.url, "youtu.be" in self.url)):
            return True if "mp4a" in format_object.acodec else False
        else:
            return True

    def _select_videos(self, video_object: modelsDL.Model) -> List[Format]:
        array_formats = video_object.formats
        check_format = lambda format_var: len([
            ft for ft in (
                "x360", "x720",
                "360x", "720x",
                "360p", "720p",
                "Direct video"
            )
            if ft in format_var]) != 0
        return [
            f for f in array_formats
            if check_format(f.format) and self._check_audio(f)
        ]

    @staticmethod
    def _is_direct(dl_object: modelsDL.Model) -> bool:
        return True if dl_object.url else False

    @property
    def _build_response(self) -> dict:
        try:
            dl = self._get_dl
            response = self._build_model(dl)
            if type(response) is list:
                log.warning(response)
                return {}

            if self._is_direct(response):
                return {
                    "duration": response.duration,
                    "title": response.title,
                    "url": response.url
                }

            videos = self._select_videos(response)

            return {
                "duration": response.duration,
                "title": response.title,
                "url": self._encrypt_link(videos[-1:][0].url)
            }
        except Exception as e:
            log.warning(e)

    @property
    def get(self) -> dict:
        return self._build_response
