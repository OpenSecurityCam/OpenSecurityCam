from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO
from onesignal_sdk.client import Client


from WebPortal.Config.ConfigFlask import Config
from WebPortal.Config.ConfigOneSignal import ConfigOneSignal

db = SQLAlchemy()
bcrypt = Bcrypt()
loginMan = LoginManager()
SocketIOClient = SocketIO()
OneSignalClient = Client(app_id=ConfigOneSignal.App_ID, rest_api_key=ConfigOneSignal.Rest_API_Key)
def create_WebPortal(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    loginMan.init_app(app)
    SocketIOClient.init_app(app)

    from WebPortal.Authentication.routes import Authentication
    from WebPortal.Usercontrol.routes import UserControl
    from WebPortal.MainPage.routes import MainPage
    from WebPortal.Notifications.routes import Notifications

    app.register_blueprint(MainPage)
    app.register_blueprint(UserControl)
    app.register_blueprint(Authentication)
    app.register_blueprint(Notifications)

    return app