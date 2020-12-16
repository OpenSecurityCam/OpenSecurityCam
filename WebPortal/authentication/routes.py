from flask import Blueprint, request, flash, redirect, render_template, url_for
from flask_login import login_user, current_user, logout_user

from WebPortal import db, bcrypt
from WebPortal.models import users
from WebPortal.authentication.forms import RegisterForm, LoginForm

authenticate = Blueprint('authentication', __name__)

@authenticate.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("Already Logged in", 'Failed')
        return redirect(url_for('main.home'))
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        foundUser = users.query.filter_by(username = loginForm.username.data).first()
        if foundUser and bcrypt.check_password_hash(foundUser.password, loginForm.password.data):
            login_user(foundUser, remember=loginForm.submit.data)
            flash("Logged in", 'Success')
            return redirect(url_for('usercontrol.userinfo'))
        else:
            flash("Login Unsuccessful", 'Failed')
    return render_template('login.html', form = loginForm)

@authenticate.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        if current_user.isAdmin == False:
            flash("Can't register, unless you're an admin", 'Failed')
            return redirect(url_for('main.home'))
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        hashedPass = bcrypt.generate_password_hash(registerForm.password.data).decode('utf-8')
        if hashedPass:
            userToAdd = users(registerForm.username.data, hashedPass)
            db.session.add(userToAdd)
            db.session.commit()
            flash("User created successfully", "Success")
            return redirect(url_for('login'))
    return render_template('register.html', form = registerForm)

@authenticate.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))