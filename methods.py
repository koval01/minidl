from flask import request
import hashlib


class Methods:

    @staticmethod
    def get_ip() -> str:
        return request.environ['HTTP_X_FORWARDED_FOR'] \
            if request.environ.get('HTTP_X_FORWARDED_FOR') \
            else request.environ['REMOTE_ADDR']

    @staticmethod
    def hash_valid(hash_string: str) -> bool:
        return hashlib.sha256(Methods.get_ip().encode("utf-8")).hexdigest() == hash_string
