from flask import Blueprint, redirect, url_for, render_template, flash, send_from_directory

from flask_login import current_user
from werkzeug.wrappers import Response

main = Blueprint('main', __name__)

@main.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('authentication.login'))  

@main.route('/<string:file_name>')
def stream(file_name):
    video_dir = './videofeed/video'
    return send_from_directory(directory=video_dir, filename=file_name)
