from flask import flash, url_for, redirect, render_template
from flask_login import login_user, current_user
from WebPortal.Authentication.Forms.LoginForm import LoginForm
from WebPortal.models import users
from WebPortal import db, bcrypt

class Validator():
    def FindUserAndLogin(self):
        # Initializing the login form
        loginForm = LoginForm()
        # Finding user
        FoundUser = users.query.filter_by(username = loginForm.username.data).first()
        # Check if a user is already logged in the current session
        if loginForm.validate_on_submit():
            # If no, login the user
            return self.__LoginUser(loginForm, FoundUser)
        else:
            return render_template('login.html', form = loginForm)

    # Logs in the user
    def __LoginUser(self, loginForm, FoundUser):
        try:
            if FoundUser:
                login_user(FoundUser, remember=loginForm.submit.data)
                flash("Logged in", 'Success')
                return redirect(url_for('UserControl.Userinfo'))
        except:
            flash("Unexpected Error", 'Failed')
            return redirect(url_for('Authentication.Login'))
            