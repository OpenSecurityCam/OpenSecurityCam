from flask.globals import request
import flask_login
from wtforms.validators import ValidationError
from auth.models import users
from flask.helpers import flash
from werkzeug.utils import redirect
from auth import app, bcrypt, db 
from flask_login import login_user, current_user, logout_user
from flask import render_template, url_for
from auth.forms import LoginForm, RegisterForm, UpdateUserForm

@app.route('/')
def main():
    if current_user.is_authenticated:
        return render_template('html/index.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("Already Logged in", 'Failed')
        return redirect(url_for('main'))
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        foundUser = users.query.filter_by(username = loginForm.username.data).first()
        if foundUser and bcrypt.check_password_hash(foundUser.password, loginForm.password.data):
            login_user(foundUser, remember=loginForm.submit.data)
            flash("Logged in", 'Success')
            return redirect(url_for('main'))
        else:
            flash("Login Unsuccessful", 'Failed')
    return render_template('html/login.html', form = loginForm)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        if current_user.isAdmin == False:
            flash("Can't register, unless you're an admin", 'Failed')
            return redirect(url_for('main'))
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        hashedPass = bcrypt.generate_password_hash(registerForm.password.data).decode('utf-8')
        if hashedPass:
            userToAdd = users(registerForm.username.data, hashedPass)
            db.session.add(userToAdd)
            db.session.commit()
            flash("User created successfully", "Success")
            return redirect(url_for('login'))
    return render_template('html/register.html', form = registerForm)

@app.route('/userinfo', methods=['GET', 'POST'])
def userinfo():
    if current_user.is_authenticated: 
        updateUserForm = UpdateUserForm()
        if updateUserForm.validate_on_submit():
            if bcrypt.check_password_hash(current_user.password, updateUserForm.password.data):
                currentUserDB = users.query.filter_by(username = current_user.username).first()
                if currentUserDB:
                    currentUserDB.username = updateUserForm.username.data
                    db.session.commit()
                    flash('Successfully changed credentials', 'Success')
                    current_user.username = updateUserForm.username.data
                else:
                    flash(f'Failed to change credentials', 'Failed')
            else:
                flash('Incorrect Password', 'Failed')
        elif request.method == 'GET':
            updateUserForm.username.data = current_user.username
            if users.query.filter(users.isAdmin.is_(False)):
                flash('SERIOUS SECURITY WARNING!!! There is still no admin account created!!', 'Warning')
        return render_template('html/userinfo.html', form=updateUserForm)
    else:
        flash("Not logged in yet", 'Failed')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))