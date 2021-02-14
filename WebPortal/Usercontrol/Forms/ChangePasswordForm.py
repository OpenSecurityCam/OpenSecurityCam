from WebPortal import bcrypt
from WebPortal.models import users

from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

# Initializing the ChangeUsernameForm class
# The class intializes a form that helps us change the username of the user
class ChangePasswordForm(FlaskForm):
    # Form Fileds
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    confirmPass = PasswordField("Repeat Password", validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
    submit = SubmitField("Change Crenetials")

    # Validates if the password is correct and if not -> raises an error that can be seen in the front-end
    def validate_password(self, password):
        foundUser = users.query.filter_by(username = current_user.username).first()
        if bcrypt.check_password_hash(current_user.password, password.data):
            raise ValidationError('No change in password!')
        