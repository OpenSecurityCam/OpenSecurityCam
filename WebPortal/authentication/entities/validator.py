from flask import flash, url_for, redirect, render_template
from flask_login import login_user

from WebPortal.authentication.forms import LoginForm
from WebPortal.models import users
from WebPortal import db, bcrypt

def FindUserAndLogin(loginForm):
    if loginForm.validate_on_submit():
        FoundUser = users.query.filter_by(username = loginForm.username.data).first()
        CheckHash = bcrypt.check_password_hash(FoundUser.password, loginForm.password.data)
        if FoundUser and CheckHash:
            login_user(FoundUser, remember=loginForm.submit.data)
            flash("Logged in", 'Success')
            return redirect(url_for('usercontrol.userinfo'))
        else:        
            flash("Login Unsuccessful", 'Failed')