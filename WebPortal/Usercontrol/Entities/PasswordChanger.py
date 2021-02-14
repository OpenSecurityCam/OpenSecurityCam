# Imports from Flask
from flask.globals import request
from flask_login import current_user
from flask import render_template, redirect, url_for, flash

# Imports from project
from WebPortal import db, bcrypt
from WebPortal.Usercontrol.Forms.ChangeUsernameForm import ChangePasswordForm
from WebPortal.models import users


# Class that updates the user's username
class PasswordChangerClass:
    # Checks if the user is logged
    #   if yes -> it goes to the __UpdateUserNameInfo method
    #   if no -> it flashes a message and redirects it to the login page
    def Main(self):
        if current_user.is_authenticated: 
            return self.__FormCheckMethod()
        else:
            flash("Not logged in yet", 'Failed')
            return redirect(url_for('Authentication.Login'))


    # Checks whether the request method is post or get
    #   if POST -> Redirects to the CheckCredentialsAndUpdateUsername 
    #   else (GET) -> Returns the HTML file with the form
    def __FormCheckMethod(self):
        userNameChangerForm = ChangePasswordForm()
        if userNameChangerForm.validate_on_submit():
            return self.__CheckCredentialsAndUpdatePassword(userNameChangerForm)
        else:
            userNameChangerForm.username.data = current_user.username
            return render_template('ChangeUsername.html', form=userNameChangerForm)


    # Checks if the user credentials are right and updates the username
    # Checks if the user is found in the database
    #   If yes -> Checks the password by using bcrypt and flashes a message if it isn't correct
    #   If not -> Flashes a message
    def __CheckCredentialsAndUpdatePassword(self, userNameChangerForm):
        currentUser = users.query.filter_by(username = current_user.username).first()
        if currentUser:
            if bcrypt.check_password_hash(currentUser.password, userNameChangerForm.password.data):
                currentUser.username = userNameChangerForm.username.data
                db.session.commit()
                flash('Successfully changed credentials', 'Success')
                return redirect(url_for('UserControl.Userinfo'))
        else:
            flash("The user currently logged in doesn't seem to be in the database.", 'Failed')
            return redirect(url_for('UserControl.UsernameChanger'))