from WebPortal import SocketIOClient
from flask import Blueprint, redirect, url_for, render_template, flash, send_from_directory
from flask_login import current_user
from werkzeug.wrappers import Response
import sys
sys.path.append('..')
from stateClass import State

MainPage = Blueprint('MainPage', __name__)


# Headers
@MainPage.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


# Main Page with the videofeed
@MainPage.route('/')
def Home():
    # Checks if the user is authenticated
    if current_user.is_authenticated:
        return render_template('index.html', SystemState = State.state)
    else:
        # If not it redirects them to the login page
        return redirect(url_for('Authentication.Login'))  

# Handles the hosting for the live stream
@MainPage.route('/<string:file_name>')
def Stream(file_name):
    # The m3u8 file directory
    video_dir = './MainPage/video'
    return send_from_directory(directory=video_dir, filename=file_name)