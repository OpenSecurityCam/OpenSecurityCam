from flask import Blueprint

from WebPortal.usercontrol.entities.userctl import UserControl
userctrl = Blueprint('usercontrol', __name__)

@userctrl.route('/userinfo', methods=['GET', 'POST'])
def userinfo():
    userctl = UserControl()
    return userctl.usercontrol()