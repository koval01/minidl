import re as regex

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
        pattern = regex.compile(r"@(s(?P<season>\d*))?(e(?P<episode>\d*))?(t(?P<translation>\d*))?")
        result = regex.search(pattern, self.url)

        try:
            result = result.groupdict()
        except AttributeError as e:
            log.error(e.__class__.__name__)
            return {"season": 1, "episode": 1, "translation": None}

        return result
        # return dict(map(
        #     lambda kv: (kv[0], regex.sub(r"\D*", "", kv[1]
        #                 if kv[1] else None)),
        #     result.items()))

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
        settings = self._get_pos
        print(settings)
        return {
            "title": self.rezka.name,
            "url":
                self._encrypt_link(
                    self._get_redirect_url(
                        self.rezka.getStream(
                            settings["season"],
                            settings["episode"],
                            settings["translation"]
                        )(480))),
            "duration": 1
        }
