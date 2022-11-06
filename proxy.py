import json

import requests
from flask import request, Response, jsonify

from cryptography.fernet import Fernet


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
            headers={key: value for (key, value) in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False)

        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items()
                   if name.lower() not in excluded_headers]

        response = Response(resp.content, resp.status_code, headers)
        return response

