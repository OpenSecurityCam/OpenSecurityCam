from flask import Blueprint, redirect, url_for, render_template

from flask_login import current_user
from werkzeug.wrappers import Response
from WebPortal.videofeed.camera import VideoCamera


main = Blueprint('main', __name__)

@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('authentication.login'))

vidstr = VideoCamera()

def gen(camera = vidstr):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@main.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')