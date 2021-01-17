from flask.helpers import flash, url_for
from flask.templating import render_template
from flask_login.utils import login_user
from werkzeug.utils import redirect

from WebPortal.authentication.forms import LoginForm
from WebPortal.models import users
from WebPortal import bcrypt

def LoginValidator(loginForm):
    FoundUser = users.query.filter_by(username = loginForm.username.data).first()
    CheckHash = bcrypt.check_password_hash(FoundUser.password, loginForm.password.data)
    if FoundUser and CheckHash:
        login_user(FoundUser, remember=loginForm.submit.data)
        flash("Logged in", 'Success')
        return redirect(url_for('usercontrol.userinfo'))
    else:        
        flash("Login Unsuccessful", 'Failed')