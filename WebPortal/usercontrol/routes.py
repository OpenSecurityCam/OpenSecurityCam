from flask import Blueprint, render_template

from WebPortal.usercontrol.entities.userctl import UserControl
userctrl = Blueprint('usercontrol', __name__)

@userctrl.route('/userinfo')
def userinfo():
    return render_template('userinfo.html')

@userctrl.route('/userinfo/credentialChanger', methods=['GET', 'POST'])
def credentialChanger():
    userctl = UserControl()
    return userctl.usercontrol()