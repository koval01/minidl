import logging as log

from flask import Flask, request

from methods import youtube, twitch

app = Flask(__name__)


@app.route('/<path:path>')
def get_video(path):
    result = None
    try:
        video_yt_id = youtube.ParserLink(f"{path}?{request.query_string.decode()}").get
        if video_yt_id:
            result = youtube.Video(video_yt_id).get

        twitch_get = twitch.Stream(path).get
        if twitch_get:
            result = twitch_get

        return result if result else {}
    except Exception as e:
        log.warning(e)
        return {}


if __name__ == '__main__':
    app.run()
