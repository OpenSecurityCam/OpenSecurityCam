from flask import Blueprint

video = Blueprint('videofeed', __name__)

@video.route('/videofeed')
def videofeed():
    return "Working"