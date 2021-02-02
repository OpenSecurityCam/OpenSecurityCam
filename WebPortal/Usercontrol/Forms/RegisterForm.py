from WebPortal.models import users

from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    confirmPassword = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
    submit = SubmitField("Register")

    def validate_username(self, username):
        foundUser = users.query.filter_by(username = username.data).first()
        if foundUser:
            raise ValidationError("User already exists")
