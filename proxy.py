import json
import os

import requests
from flask import request, Response, jsonify, stream_with_context

from cryptography.fernet import Fernet

PROXIES = {
    'http': 'socks5://92.101.95.210:1080',
    'https': 'socks5://92.101.95.210:1080'
}
# test proxy


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

        print(url)

        resp = requests.request(
            method=request.method,
            url=url,
            proxies=PROXIES,
            headers={key: value for (key, value) in request.headers if key != 'Host'},
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

