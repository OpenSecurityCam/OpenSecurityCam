from flask import Blueprint, render_template

from WebPortal.Usercontrol.Entities.UsernameChanger import UsernameChangerClass
from WebPortal.Usercontrol.Entities.Registrator import RegistratorClass

UserControl = Blueprint('UserControl', __name__)

@UserControl.route('/userinfo')
def Userinfo():
    return render_template('UserInfo.html')

@UserControl.route('/userinfo/usernameChanger', methods=['GET', 'POST'])
def UsernameChanger():
    usernamechanger = UsernameChangerClass()
    return usernamechanger.Main()

@UserControl.route('/userinfo/register', methods=['GET', 'POST'])
def RegisterUser():
    registrator = RegistratorClass()
    return registrator.RegisterUser()