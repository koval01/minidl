import logging as log
import os
import sys
from time import time

import psutil
import platform
import requests
from flask import Flask, request, jsonify, __version__ as flask_ver

import DL
import proxy
import rezka

app = Flask(__name__)
secret_key = os.getenv("SECRET_KEY").encode()


@app.route('/')
def empty():
    return {}


@app.route('/node')
def node():
    if os.getenv("DEBUG"):
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = lambda load: round((load / os.cpu_count()) * 100)

        return jsonify({
            "host": request.host,
            "ip": requests.get("https://ident.me").text,
            "flask": flask_ver,
            "python": sys.version,
            "cpu_load": {
                "load1": cpu_usage(load1),
                "load5": cpu_usage(load5),
                "load15": cpu_usage(load15)
            },
            "ram_percent": round(psutil.virtual_memory()[2]),
            "time": round(time()),
            "platform": platform.platform()
        })
    return {}


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
