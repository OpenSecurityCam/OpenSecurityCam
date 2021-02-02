from flask import flash, url_for, redirect, render_template
from flask_login import login_user, current_user
from WebPortal.Authentication.Forms.LoginForm import LoginForm
from WebPortal.models import users
from WebPortal import db, bcrypt

class Validator():
    def FindUserAndLogin(self):
        loginForm = LoginForm()
        if current_user.is_authenticated:
            self.__UserIsLoggedIn()
        if loginForm.validate_on_submit():
            return self.__FindUser(loginForm)
        return render_template('login.html', form = loginForm)

    def __UserIsLoggedIn(self):
        flash("Already Logged in", 'Failed')

    def __FindUser(self, loginForm):
        try:
            FoundUser = users.query.filter_by(username = loginForm.username.data).first()
            CheckHash = bcrypt.check_password_hash(FoundUser.password, loginForm.password.data)
            login_user(FoundUser, remember=loginForm.submit.data)
            flash("Logged in", 'Success')
            return redirect(url_for('UserControl.Userinfo'))
        except:
            flash("Login Unsuccessful", 'Failed')
            return redirect(url_for('Authentication.Login'))
            