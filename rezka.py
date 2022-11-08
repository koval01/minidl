import re as regex

import requests
from flask import request

import proxy
from HdRezkaApi import *


class Rezka:

    def __init__(self, secret_key: bytes, url: str) -> None:
        self.secret_key: bytes = secret_key
        self.url: str = url
        self.rezka = HdRezkaApi(url)

    @property
    def _get_pos(self) -> dict:
        pattern = regex.compile(r"@s(?P<season>\d)e(?P<episode>\d)")
        result = regex.search(pattern, self.url)
        print(result)
        return {}

    def _encrypt_link(self, source_url: str) -> str:
        return "%smedia_proxy/%s" % (
            request.host_url,
            proxy.Proxy(self.secret_key).encrypt_url(source_url)
        )

    @staticmethod
    def _get_redirect_url(url: str) -> str:
        return requests.get(
            url, allow_redirects=False,
            proxies=proxy.PROXIES
        ).headers["Location"]

    @property
    def get(self) -> dict:
        return {
            "title": self.rezka.name,
            "url":
                self._encrypt_link(
                    self._get_redirect_url(
                        self.rezka.getStream(1, 1)(480))),
            "duration": self.rezka.id
        }
