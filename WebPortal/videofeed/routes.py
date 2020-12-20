from flask import Blueprint, redirect, url_for, render_template, flash

from flask_login import current_user
from werkzeug.wrappers import Response
from WebPortal import gen

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('authentication.login'))

@main.route('/video_feed')
def video_feed():
    try:
        return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
    except :
        pass
    