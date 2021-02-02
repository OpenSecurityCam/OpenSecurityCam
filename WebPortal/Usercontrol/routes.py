from flask import Blueprint, render_template

from WebPortal.Usercontrol.Entities.Userctl import UserControl as uc
from WebPortal.Usercontrol.Entities.Registrator import Registrator

UserControl = Blueprint('UserControl', __name__)

@UserControl.route('/userinfo')
def Userinfo():
    return render_template('userinfo.html')

@UserControl.route('/userinfo/usernameChanger', methods=['GET', 'POST'])
def UsernameChanger():
    userctl = uc()
    return userctl.usercontrol()

@UserControl.route('/userinfo/register', methods=['GET', 'POST'])
def RegisterUser():
    registrator = Registrator()
    return registrator.RegisterUser()