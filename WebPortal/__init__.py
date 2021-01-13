from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from WebPortal.config import Config
from WebPortal.videofeed.camera import Cam

db = SQLAlchemy()
bcrypt = Bcrypt()
loginMan = LoginManager()
def create_WebPortal(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    loginMan.init_app(app)

    from WebPortal.authentication.routes import authenticate
    from WebPortal.usercontrol.routes import userctrl
    from WebPortal.videofeed.routes import main

    app.register_blueprint(authenticate)
    app.register_blueprint(main)
    app.register_blueprint(userctrl)
    app.register_blueprint(main)

    return app