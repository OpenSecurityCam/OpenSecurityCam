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

    def __FindUser(self):
        foundUser = users.query.filter_by(username = self.username.data).first()
        return foundUser

    def validate_formUsername(self, username):
        if self.__FindUser() is None:
            raise ValidationError('Username not found')

    def validate_formPassword(self, password):
        if bcrypt.check_password_hash(self.__FindUser().password, password.data) == False:
            raise ValidationError(password.data)