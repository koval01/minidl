import logging as log

from flask import Flask, request

from methods import youtube, twitch

app = Flask(__name__)


@app.route('/')
def empty():
    return {}


@app.route('/<path:path>')
def get_video(path):
    try:
        full_url = f"{path}?{request.query_string.decode()}"

        video_yt_id = youtube.ParserLink(full_url).get
        if video_yt_id:
            result = youtube.Video(video_yt_id).get
            if result:
                return result

        twitch_get = twitch.Stream(path).get
        if twitch_get:
            result = twitch_get
            if result:
                return result

        return {}
    except Exception as e:
        log.warning(e)
        return {}


if __name__ == '__main__':
    app.run()
