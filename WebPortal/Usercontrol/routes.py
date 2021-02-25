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

UserControl = Blueprint('UserControl', __name__)

@UserControl.route('/userinfo')
def Userinfo():
    # profilePic = url_for('static', )
    return render_template('UserInfo.html')

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

@UserControl.route('/userinfo/ChangeProfilePicture/<user>', methods=['GET', 'POST'])
def ChangeProfilePic(user):
    if request.method == 'POST':
        
        return f"Hey, it's working. You are {user}"


@UserControl.route('/logout')
def Logout():
    logout_user()
    return redirect(url_for('Authentication.Login'))
