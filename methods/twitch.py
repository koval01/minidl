from urllib.parse import urlparse

import streamlink
from streamlink.plugins.twitch import TwitchHLSStream


class Stream:

    def __init__(self, stream_url: str) -> None:
        self.stream_url: str = stream_url

    @property
    def _get_data(self) -> TwitchHLSStream or None:
        try:
            if self._link_check:
                return streamlink.streams(self.stream_url)["best"]
        except KeyError:
            return None

    @property
    def _get_username(self) -> str or None:
        try:
            return urlparse(self.stream_url).path.split("/")[1]
        except IndexError:
            return None

    @property
    def _link_check(self) -> bool:
        return True if "twitch.tv" in self.stream_url else False

    @property
    def get(self) -> dict:
        stream = self._get_data
        return {
            "url": stream.url,
            "title": self._get_username
        } if stream else {}
