from flask import Blueprint, request, flash, redirect, render_template, url_for
from flask_login import login_user, current_user, logout_user

from WebPortal import db, bcrypt
from WebPortal.models import users
from WebPortal.authentication.forms import RegisterForm, LoginForm
from WebPortal.authentication.entities.validator import LoginValidator
from WebPortal.authentication.entities.registrator import RegisterUser, CheckIfUserIsAdmin

authenticate = Blueprint('authentication', __name__)

@authenticate.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("Already Logged in", 'Failed')
        return redirect(url_for('main.home'))
    else:
        loginForm = LoginForm()
        if loginForm.validate_on_submit():
            LoginValidator(loginForm)
    return render_template('login.html', form = loginForm)

@authenticate.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        if current_user.isAdmin == False:
            flash("Can't register, unless you're an admin", 'Failed')
            return redirect(url_for('main.home'))
    registerForm = RegisterForm()
    RegisterUser(registerForm)
    return render_template('register.html', form = registerForm)

@authenticate.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))