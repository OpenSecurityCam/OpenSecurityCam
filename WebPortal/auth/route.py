from auth.models import users
from flask.helpers import flash
from werkzeug.utils import redirect
from auth import app, bcrypt, db 
from flask_login import login_user, current_user, logout_user
from flask import render_template, url_for
from auth.forms import LoginForm, RegisterForm

@app.route('/')
def main():
    if current_user.is_authenticated:
        return render_template('html/index.html', userInfo = current_user.username)
    else:
        return render_template('html/index.html')

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
        flash("Already Logged in", 'Failed')
        return redirect(url_for('main'))
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        hashedPass = bcrypt.generate_password_hash(registerForm.password.data).decode('utf-8')
        userToAdd = users(registerForm.username.data, hashedPass)
        db.session.add(userToAdd)
        db.session.commit()
        flash("User created successfully", "Success")
        return redirect(url_for('login'))
    return render_template('html/register.html', form = registerForm)

@app.route('/userinfo')
def userinfo():
    pass

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))