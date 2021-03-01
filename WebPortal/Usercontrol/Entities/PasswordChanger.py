# Imports from Flask
from flask.globals import request
from flask_login import current_user
from flask import render_template, redirect, url_for, flash

# Imports from project
from WebPortal import db, bcrypt
from WebPortal.Usercontrol.Forms.ChangePasswordForm import ChangePasswordForm
from WebPortal.models import users


# Class that updates the user's username
class PasswordChangerClass:

    # Constructor
    def __init__(self, user):
        self.user = user

    # Main Function
    def Main(self):
        if current_user.is_authenticated: 
            return self.__FormCheckMethod()
        else:
            flash("Not logged in yet", 'Failed')
            return redirect(url_for('Authentication.Login'))


    # Finds the user giving user string 
    def __User(self):
        return users.query.filter_by(username = self.user).first()

    # Checks the method of the form
    def __FormCheckMethod(self):
        # Initializes the form giving it user as a value
        passwordChangerForm = ChangePasswordForm(self.__User())
        # Checks the request.method
        if passwordChangerForm.validate_on_submit():
            return self.__CheckCredentialsAndUpdatePassword(passwordChangerForm)
        else:
            return render_template('ChangePassword.html', form=passwordChangerForm)

    # Checks the credentials and updated the username
    def __CheckCredentialsAndUpdatePassword(self, passwordChangerForm):
        try:
            if self.__User():
                # Generates the new password hash
                self.__User().password = bcrypt.generate_password_hash(passwordChangerForm.confirmPass.data).decode('utf-8')
                db.session.commit()
                flash('Password changed successfully', 'Success')
                return redirect(url_for('UserControl.AdminPanel'))
            else:
                flash("The user currently logged in doesn't seem to be in the database.", 'Failed')
                return redirect(url_for('UserControl.Logout'))
        except:
            flash("Internal Error", 'Failed')
        