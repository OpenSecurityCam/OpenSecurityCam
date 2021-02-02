from WebPortal.models import users

from flask_wtf import FlaskForm
from wtforms.fields.core import BooleanField, StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    stayLoggedIn = BooleanField("Remember Me")
    submit = SubmitField("Log In")