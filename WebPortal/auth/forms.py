from auth.models import users
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms.fields.core import BooleanField, StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from flask_login import current_user

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    confirmPassword = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
    submit = SubmitField("Register")

    def validate_username(self, username):
        foundUser = users.query.filter_by(username = username.data).first()
        if foundUser:
            raise ValidationError("User already exists")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    stayLoggedIn = BooleanField("Remember Me")
    submit = SubmitField("Log In")

class UpdateUserForm(FlaskForm):
    username = StringField("Change Username", validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    confirmPass = PasswordField("Repeat Password", validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
    submit = SubmitField("Change Crenetials")

    def validate_username(self, username):
        if username.data == current_user.username:
            raise ValidationError('No change in username')
        elif users.query.filter_by(username = username.data).first():
            raise ValidationError('Username already exists')
    