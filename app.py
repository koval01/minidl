import logging as log

import requests
from flask import Flask, request, __version__ as flask_ver
import os

import DL
import rezka
import proxy

app = Flask(__name__)
secret_key = os.getenv("SECRET_KEY").encode()


@app.route('/')
def empty():
    return {}


@app.route('/node')
def node():
    return {
        "host": request.host,
        "ip": requests.get("https://ident.me").text,
        "app": flask_ver
    }


@app.route('/media_proxy/<path:token>')
def media_proxy(token):
    return proxy.Proxy(secret_key, token).request


@app.route('/<path:path>')
def get_video(path):
    try:
        full_url = f"{path}?{request.query_string.decode()}"
        if "rezka." in path:
            obj = rezka.Rezka(secret_key, full_url).get
        else:
            obj = DL.Video(secret_key, full_url).get
        return obj if obj else {}
    except Exception as e:
        log.warning(e)
        return {}


if __name__ == '__main__':
    app.run()
