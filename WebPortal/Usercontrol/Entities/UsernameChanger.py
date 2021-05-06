# Imports from Flask
from flask.globals import request
from flask_login import current_user
from flask import render_template, redirect, url_for, flash

# Imports from project
from WebPortal import db
from WebPortal.Usercontrol.Forms.ChangeUsernameForm import ChangeUsernameForm
from WebPortal.models import users


class UsernameChangerClass:
    # Constructor
    def __init__(self, user):
        self.user = user

    # Finds the user giving user string 
    def __User(self):
        return users.query.filter_by(username = self.user).first()

    # Main Function
    def Main(self):
        if current_user.is_authenticated: 
            # Initializes the form giving it user as a value
            usernameChangerForm = ChangeUsernameForm(self.__User())
            # Checks the request.method
            if request.method == "POST":
                return self.__ChangeUsername(usernameChangerForm)
            else:
                return render_template('ChangeUsername.html', form=usernameChangerForm, userToChange = self.__User().username)
        else:
            flash("Not logged in yet", 'Failed')
            return redirect(url_for('Authentication.Login'))

    # Checks the credentials and updated the username
    def __ChangeUsername(self, usernameChangerForm):
        try:
            if self.__User():
                self.__User().username = usernameChangerForm.username.data
                db.session.commit()
                flash('Successfully changed credentials', 'Success')
                return redirect(url_for('UserControl.AdminPanel'))
            else:
                flash("The user currently logged in doesn't seem to be in the database.", 'Failed')
                return redirect(url_for('UserControl.Logout'))
        except:
            flash("Internal Error", 'Failed')