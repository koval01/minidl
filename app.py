import logging as log

from flask import Flask, request

from methods import ParserLink, Video

app = Flask(__name__)


@app.route('/<path:path>')
def get_video(path):
    try:
        video_id = ParserLink(f"{path}?{request.query_string.decode()}").get
        if video_id:
            return Video(video_id).get
        return {}
    except Exception as e:
        log.warning(e)
        return {}


if __name__ == '__main__':
    app.run()
