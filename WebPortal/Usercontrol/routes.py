from flask import Blueprint, render_template

from WebPortal.Usercontrol.Entities.UsernameChanger import UsernameChangerClass
from WebPortal.Usercontrol.Entities.PasswordChanger import PasswordChangerClass
from WebPortal.Usercontrol.Entities.Registrator import RegistratorClass

from WebPortal.models import users

UserControl = Blueprint('UserControl', __name__)

@UserControl.route('/userinfo')
def Userinfo():
    return render_template('UserInfo.html')

@UserControl.route('/userinfo/UsernameChanger/<user>', methods=['GET', 'POST'])
def UsernameChange(user):
    usernamechanger = UsernameChangerClass()
    return usernamechanger.Main(user)

@UserControl.route('/userinfo/ChangePassword/<user>', methods=['GET', 'POST'])
def PasswordChange(user):
    passwordchanger = PasswordChangerClass()
    return passwordchanger.Main(user)

@UserControl.route('/userinfo/Register', methods=['GET', 'POST'])
def RegisterUser():
    registrator = RegistratorClass()
    return registrator.RegisterUser()

@UserControl.route('/userinfo/Users')
def UsersControl():
    users1 = users.query.all()
    return render_template('UserControl.html', Users = users1)