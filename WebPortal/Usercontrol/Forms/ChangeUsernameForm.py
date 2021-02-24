from WebPortal import bcrypt
from WebPortal.models import users

from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

# Initializing the ChangeUsernameForm class
# The class intializes a form that helps us change the username of the user
class ChangeUsernameForm(FlaskForm):
    # Form Fileds
    username = StringField("Change Username", validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    confirmPass = PasswordField("Repeat Password", validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
    submit = SubmitField("Change Crenetials")

    def __init__(self, foundUser, *args, **kwargs):
        self.foundUser = foundUser
        super(ChangeUsernameForm, self).__init__(*args, **kwargs)
    
    # Validates if the username already exists in the database or if there's no change and if so -> raises a error that can be seen in the front-end
    def validate_username(self, username):
        if username.data == self.foundUser.username:
            raise ValidationError('No change in username. Try again')
        elif users.query.filter_by(username = username.data).first():
            raise ValidationError('Username already exists')

    # Validates if the password is correct and if not -> raises an error that can be seen in the front-end
    def validate_password(self, password):
        if bcrypt.check_password_hash(self.foundUser.password, password.data) == False:
            raise ValidationError('The password is incorrect. Please try again!')

