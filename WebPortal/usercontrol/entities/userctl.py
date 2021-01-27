from flask_login import current_user
from flask import render_template, request, redirect, url_for, flash

from WebPortal import db, bcrypt
from WebPortal.usercontrol.forms import UpdateUserForm
from WebPortal.models import users

class UserControl:
    def usercontrol(self):
        if current_user.is_authenticated: 
            return self.UpdateUserInfo()
        else:
            flash("Not logged in yet", 'Failed')
            return redirect(url_for('login'))

    def UpdateUserInfo(self):
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
            if users.query.filter(users.isAdmin) == 0:
                flash('SERIOUS SECURITY WARNING!!! There is still no admin account created!!', 'Warning')
            return render_template('changeUserCredentials.html', form=updateUserForm)