import bcrypt
from WebPortal.models import users
from WebPortal import bcrypt

from flask_wtf import FlaskForm
from wtforms.fields.core import BooleanField, StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    stayLoggedIn = BooleanField("Remember Me")
    submit = SubmitField("Log In")

    def FindUser(self):
        foundUser = users.query.filter_by(username = self.username.data).first()
        return foundUser

    def validate_username(self, username):
        foundUser = self.FindUser()
        if foundUser is None:
            print('Im here')
            raise ValidationError('Username not found')

    def validate_password(self, password):
        foundUser = self.FindUser()
        if bcrypt.check_password_hash(foundUser.password, password.data) == False:
            raise ValidationError('Incorrect Password')