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
    # Checks if the user is logged
    #   if yes -> it goes to the __UpdateUserNameInfo method
    #   if no -> it flashes a message and redirects it to the login page
    def Main(self, usernameToCheck):
        if current_user.is_authenticated: 
            return self.__FormCheckMethod(usernameToCheck)
        else:
            flash("Not logged in yet", 'Failed')
            return redirect(url_for('Authentication.Login'))


    # Checks whether the request method is post or get
    #   if POST -> Redirects to the CheckCredentialsAndUpdateUsername 
    #   else (GET) -> Returns the HTML file with the form
    def __FormCheckMethod(self, usernameToCheck):
        foundUser = users.query.filter_by(username = usernameToCheck).first()
        passwordChangerForm = ChangePasswordForm(foundUser)
        if passwordChangerForm.validate_on_submit():
            return self.__CheckCredentialsAndUpdatePassword(passwordChangerForm, foundUser)
        else:
            return render_template('ChangePassword.html', form=passwordChangerForm, userToChange = foundUser.username)


    # Checks if the user credentials are right and updates the username
    # Checks if the user is found in the database
    #   If yes -> Checks the password by using bcrypt and flashes a message if it isn't correct
    #   If not -> Flashes a message
    def __CheckCredentialsAndUpdatePassword(self, passwordChangerForm, foundUser):
        try:
            if foundUser:
                foundUser.password = bcrypt.generate_password_hash(passwordChangerForm.confirmPass.data).decode('utf-8')
                db.session.commit()
                flash('Password changed successfully', 'Success')
                return redirect(url_for('UserControl.AdminPanel'))
            else:
                flash("The user currently logged in doesn't seem to be in the database.", 'Failed')
                return redirect(url_for('UserControl.Logout'))
        except:
            flash("Internal Error", 'Failed')
        