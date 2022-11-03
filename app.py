from flask import Flask
import youtube_dl

app = Flask(__name__)


@app.route('/<video_id>')
def get_video(video_id):
    with youtube_dl.YoutubeDL() as ydl:
        return ydl.extract_info(
            'https://www.youtube.com/watch?v=%s' % video_id,
            download=False
        )


if __name__ == '__main__':
    app.run()
