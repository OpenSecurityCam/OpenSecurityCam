from flask import Blueprint, request, flash, redirect, render_template, url_for
from flask_login import login_user, current_user, logout_user

from WebPortal.Authentication.Forms.LoginForm import LoginForm
from WebPortal.Authentication.Entities.Validator import Validator

Authentication = Blueprint('Authentication', __name__)

@Authentication.route('/login', methods=['GET', 'POST'])
def Login():
    validator = Validator()
    return validator.FindUserAndLogin()

@Authentication.route('/logout')
def Logout():
    logout_user()
    return redirect(url_for('Authentication.Login'))
