from WebPortal.models import users

from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

class ChangeUsernameForm(FlaskForm):
    username = StringField("Change Username", validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=20)])
    confirmPass = PasswordField("Repeat Password", validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
    submit = SubmitField("Change Crenetials")

    def validate_username(self, username):
        if username.data == current_user.username:
            raise ValidationError('No change in username. Try again')
        elif users.query.filter_by(username = username.data).first():
            raise ValidationError('Username already exists')

