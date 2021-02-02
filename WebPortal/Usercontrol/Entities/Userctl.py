from flask_login import current_user
from flask import render_template, request, redirect, url_for, flash

from WebPortal import db, bcrypt
from WebPortal.Usercontrol.Forms.ChangeUsernameForm import ChangeUsernameForm
from WebPortal.models import users

class UserControl:
    def usercontrol(self):
        if current_user.is_authenticated: 
            return self.UpdateUserInfo()
        else:
            flash("Not logged in yet", 'Failed')
            return redirect(url_for('Authentication.Login'))

    def UpdateUserInfo(self):
        userNameChangerForm = ChangeUsernameForm()
        if userNameChangerForm.validate_on_submit():
            currentUserDB = users.query.filter_by(username = current_user.username).first()
            if currentUserDB:
                if bcrypt.check_password_hash(current_user.password, userNameChangerForm.password.data):
                    currentUserDB.username = userNameChangerForm.username.data
                    db.session.commit()
                    flash('Successfully changed credentials', 'Success')
                    return redirect(url_for('UserControl.Userinfo'))
                else:
                    flash(f'Failed to change credentials', 'Failed')
            else:
                flash('Incorrect Password', 'Failed')
        elif request.method == 'GET':
            userNameChangerForm.username.data = current_user.username
            return render_template('changeUserCredentials.html', form=userNameChangerForm)