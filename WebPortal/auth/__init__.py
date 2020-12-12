from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'gdfgdfgsdgsgsd534534'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/LibreSecurityCam'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

loginMan = LoginManager(app)

from auth.route import *
