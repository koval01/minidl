import json
import os

import urllib.parse

import requests
from flask import request, Response, jsonify, stream_with_context

from cryptography.fernet import Fernet

env_proxy = os.getenv("PROXY_URL")
PROXIES = {
    'http': env_proxy,
    'https': env_proxy
}
HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Dnt': '1', 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Sec-Fetch-Site': 'none', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document', 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'uk,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
}


class Proxy:

    def __init__(self, key: bytes, token: str = None) -> None:
        self.fer = Fernet(key)
        self.token: str = token

    @property
    def _get_url(self) -> str:
        raw = self.fer.decrypt(self.token)
        body = json.loads(raw.decode("utf-8"))
        return body["url"]

    def encrypt_url(self, url: str) -> str:
        body = json.dumps({
            "url": url
        })
        raw = self.fer.encrypt(body.encode("utf-8"))
        return raw.decode("utf-8")

    @property
    def request(self) -> Response or jsonify:
        url = self._get_url
        if not url:
            return jsonify({})

        headers = {
            key: value for (key, value) in request.headers
            if (key != 'Host' and "X-" not in key)
        }
        headers = {**headers, **HEADERS, "Host": urllib.parse.urlparse(url).netloc}
        if headers.get("Cookie"):
            del headers["Cookie"]

        print(headers)

        resp = requests.request(
            method=request.method,
            url=url,
            proxies=PROXIES,
            headers=headers,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            stream=True)

        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items()
                   if name.lower() not in excluded_headers]

        response = Response(
            stream_with_context(resp.iter_content(chunk_size=1024)),
            resp.status_code, headers)
        return response

