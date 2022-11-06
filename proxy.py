import requests
from flask import request, Response, jsonify


class Proxy:

    def __init__(self, path: str, zalupa_token: str) -> None:
        self.path = path
        self.zalupa_token = zalupa_token

    @property
    def _check_token(self) -> bool:
        return True

    def proxy(self, *args, **kwargs) -> Response or jsonify:
        if not self._check_token:
            return jsonify({})

        resp = requests.request(
            method=request.method,
            url=f"{self.path}?{request.query_string.decode()}",
            headers={key: value for (key, value) in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False)

        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items()
                   if name.lower() not in excluded_headers]

        response = Response(resp.content, resp.status_code, headers)
        return response

