from flask import Blueprint, redirect, url_for, render_template, flash

from flask_login import current_user
from werkzeug.wrappers import Response
import cv2
from WebPortal.videofeed.camera import Cam

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('authentication.login'))

# def get_frame():
#     camera=cv2.VideoCapture(0) #this makes a web cam object

#     while True:
#         retval, im = camera.read()
#         imgencode=cv2.imencode('.jpg',im)[1]
#         stringData=imgencode.tobytes()
#         yield (b'--frame\r\n'
#             b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
    
#     del(camera)

@main.route('/video_feed')
def video_feed():
    return Response(Cam.get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    