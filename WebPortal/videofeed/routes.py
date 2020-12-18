from flask import Blueprint, redirect, url_for, render_template, flash

from flask_login import current_user
from werkzeug.wrappers import Response
from WebPortal.videofeed.camera import VideoCamera

main = Blueprint('main', __name__)

video_stream = VideoCamera()

@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('authentication.login'))

def gen(stream):
    while True:
        frame = stream.get_frame()
        yield (frame)

@main.route('/video_feed')
def video_feed():
        return Response(gen(video_stream))
    