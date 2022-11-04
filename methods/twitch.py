from urllib.parse import urlparse
from bs4 import BeautifulSoup
from requests import get as http_get

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
    def _get_page(self) -> BeautifulSoup or None:
        resp = http_get(self.stream_url)
        if resp.status_code <= 299:
            return BeautifulSoup(resp.content.decode('utf-8'))

    @staticmethod
    def _get_meta(soup: BeautifulSoup, property_="og:video:duration") -> str or None:
        tag = soup.find("meta", property=property_)
        return tag["content"] if tag else None

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
        result = {
            "url": stream.url,
            "title": self._get_username
        } if stream else {}

        if (stream.url.split(".")[-1:][0]).lower() != "m3u8":
            body = self._get_page
            result["duration"] = int(self._get_meta(body))
            result["title"] = self._get_meta(body, "og:title")

        return result
