from flask import Blueprint, request, flash, redirect, render_template, url_for
from flask_login import login_user, current_user, logout_user

from WebPortal.authentication.forms import RegisterForm, LoginForm
from WebPortal.authentication.entities.validator import Validator
from WebPortal.authentication.entities.registrator import Registrator

authenticate = Blueprint('authentication', __name__)

@authenticate.route('/login', methods=['GET', 'POST'])
def login():
    validator = Validator()
    return validator.FindUserAndLogin()

@authenticate.route('/register', methods=['GET', 'POST'])
def register():
    registrator = Registrator()
    return registrator.RegisterUser()
    

@authenticate.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
