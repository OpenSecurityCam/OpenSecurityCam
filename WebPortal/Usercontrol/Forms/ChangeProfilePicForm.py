from wtforms.fields.simple import SubmitField
from WebPortal import bcrypt
from WebPortal.models import users

from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import Length, Optional

# Initializing the ChangeProfilePictureForm class
# The class intializes a form that helps us change the username of the user
class ChangeProfilePictureForm(FlaskForm):
    # Form Fileds
    profilePicture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'], 'File Not Allowed')])
    submit = SubmitField("Change Profile Picture")