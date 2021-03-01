# Imports from Flask
from flask.globals import request
from flask_login import current_user
from flask import render_template, redirect, url_for, flash

# Imports from project
from WebPortal import db, bcrypt
from WebPortal.Usercontrol.Forms.ChangeUsernameForm import ChangeUsernameForm
from WebPortal.models import users


class UsernameChangerClass:
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
        userNameChangerForm = ChangeUsernameForm(self.__User())
        # Checks the request.method
        if userNameChangerForm.validate_on_submit():
            return self.__CheckCredentialsAndUpdateUsername(userNameChangerForm)
        else:
            return render_template('ChangeUsername.html', form=userNameChangerForm, userToChange = self.__User().username)


    # Checks the credentials and updated the username
    def __CheckCredentialsAndUpdateUsername(self, userNameChangerForm):
        if self.__User():
            # Checks if the password hash is equal to the given password in the form
            if bcrypt.check_password_hash(self.__User().password, userNameChangerForm.password.data):
                db.session.commit()
                flash('Successfully changed credentials', 'Success')
                return redirect(url_for('UserControl.AdminPanel'))
        else:
            flash("The user currently logged in doesn't seem to be in the database.", 'Failed')
            return redirect(url_for('Authentication.Login'))