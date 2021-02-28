from flask.globals import request
from flask_login.utils import logout_user
from werkzeug.utils import redirect
from WebPortal.models import users
from flask import Blueprint, render_template
from flask.helpers import flash, url_for
from flask_login import current_user

from WebPortal.Usercontrol.Entities.UsernameChanger import UsernameChangerClass
from WebPortal.Usercontrol.Entities.PasswordChanger import PasswordChangerClass
from WebPortal.Usercontrol.Entities.Registrator import RegistratorClass
from WebPortal.Usercontrol.Entities.AdminPanel import AdminPanelClass
from WebPortal.Usercontrol.Entities.RightsChanger import RightsChangerClass
from WebPortal.Usercontrol.Entities.DeleteUser import DeleteUserClass

from WebPortal.Usercontrol.Forms.ChangeProfilePicForm import ChangeProfilePictureForm
import secrets
from PIL import Image
import os
from WebPortal import db

UserControl = Blueprint('UserControl', __name__)

@UserControl.route('/userinfo', methods=['GET', 'POST'])
def Userinfo():
    cppf = ChangeProfilePictureForm()
    if request.method == 'POST':
        foundUser = users.query.filter_by(username = current_user.username).first()
        if cppf.profilePicture.data:
            foundUser.profilePicture = save_picture(cppf.profilePicture.data)
            db.session.commit()
        else:
            foundUser.profilePicture = 'default.png'
            db.session.commit()
    return render_template('UserInfo.html', form = cppf)

@UserControl.route('/userinfo/AdminPanel')
def AdminPanel():
    return AdminPanelClass.AdminPanel()

@UserControl.route('/userinfo/AdminPanel/GiveAdminRights/<user>', methods=['GET', 'POST'])
def GiveAdminRights(user):
    RightsChanger = RightsChangerClass(user)
    return RightsChanger.RightsChanger()

@UserControl.route('/userinfo/AdminPanel/DeleteUser/<user>', methods=['GET', 'POST'])
def DeleteUser(user):
    DelUser = DeleteUserClass(user)
    return DelUser.DeleteUser()

@UserControl.route('/userinfo/AdminPanel/Register', methods=['GET', 'POST'])
def RegisterUser():
    registrator = RegistratorClass()
    return registrator.RegisterUser()

@UserControl.route('/userinfo/UsernameChanger/<user>', methods=['GET', 'POST'])
def UsernameChange(user):
    usernamechanger = UsernameChangerClass()
    return usernamechanger.Main(user)

@UserControl.route('/userinfo/ChangePassword/<user>', methods=['GET', 'POST'])
def PasswordChange(user):
    passwordchanger = PasswordChangerClass()
    return passwordchanger.Main(user)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join('WebPortal/static/profilePics', picture_fn)

    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

# @UserControl.route('/userinfo/ChangeProfilePicture/<user>', methods=['GET', 'POST'])
# def ChangeProfilePic(user):


@UserControl.route('/logout')
def Logout():
    logout_user()
    return redirect(url_for('Authentication.Login'))
