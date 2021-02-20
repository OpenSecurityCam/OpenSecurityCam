from WebPortal import bcrypt
from WebPortal.models import users

from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

# Initializing the ChangeUsernameForm class
# The class intializes a form that helps us change the username of the user
class ChangePasswordForm(FlaskForm):
    # Form Fileds
    currentPassword = PasswordField("Current Password", validators=[DataRequired(),Length(min=6, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    confirmPass = PasswordField("Repeat Password", validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
    submit = SubmitField("Change Password")

    # Validates the current password
    def validate_currentPassword(self, currentPassword):
        if current_user.password == currentPassword.data and current_user.isAdmin == False:
            raise ValidationError('Wrong Password. Please contact the admin for assistance.')

    # Validates if the password is correct and if not -> raises an error that can be seen in the front-end
    def validate_password(self, password):
        if password.data == current_user.password:
            raise ValidationError('No change in password!')
        