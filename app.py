import logging as log

from flask import Flask, request
from cryptography.fernet import Fernet

import DL

app = Flask(__name__)


@app.route('/')
def empty():
    return {}


@app.route('/<path:path>')
def get_video(path):
    try:
        obj = DL.Video(f"{path}?{request.query_string.decode()}").get
        return obj if obj else {}
    except Exception as e:
        log.warning(e)
        return {}


if __name__ == '__main__':
    app.run()
