import logging as log

from flask import Flask, request
from cryptography.fernet import Fernet

import DL
import proxy

app = Flask(__name__)
secret_key = Fernet.generate_key()


@app.route('/')
def empty():
    return {}


@app.route('/media_proxy/<path:token>')
def media_proxy(token):
    return proxy.Proxy(secret_key, token).request


@app.route('/<path:path>')
def get_video(path):
    try:
        obj = DL.Video(secret_key, f"{path}?{request.query_string.decode()}").get
        return obj if obj else {}
    except Exception as e:
        log.warning(e)
        return {}


if __name__ == '__main__':
    app.run()
