import logging as log
import os

import validators
from dotenv import load_dotenv
from flask import Flask, request

import DL
import proxy
import rezka
from HdRezkaApi import *
from methods import Methods

load_dotenv()

log.basicConfig(
    level=log.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - \"%(message)s\"",
    datefmt="%H:%M:%S"
)

app = Flask(__name__)
secret_key = os.getenv("SECRET_KEY").encode()


@app.route('/')
def empty():
    return {}


@app.route('/ip')
def get_ip():
    return {"ip": Methods.get_ip()}


@app.route('/ip/<hash_string>')
def hash_valid(hash_string: str):
    return {"valid": Methods.hash_valid(hash_string)}


@app.route('/media_proxy/<path:token>')
def media_proxy(token: str):
    return proxy.Proxy(secret_key, token).request


@app.route('/rezka/translations/<path:path>')
def rezka_translations(path: str):
    return HdRezkaApi(f"{path}?{request.query_string.decode()}").getTranslations()


@app.route('/<path:path>')
def get_video(path: str):
    # try:
        full_url = f"{path}?{request.query_string.decode()}"
        if not validators.url(full_url):
            return {}
        if "rezka." in path:
            obj = rezka.Rezka(secret_key, full_url).get
        else:
            obj = DL.Video(secret_key, full_url).get
        return obj if obj else {}
    # except Exception as e:
    #     log.warning(e)
    #     return {}


if __name__ == '__main__':
    app.run()
