from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from flask_login import current_user

from WebPortal import db, bcrypt
from WebPortal.models import users

def RegisterUser(registerForm):
    if registerForm.validate_on_submit():
        hashedPass = bcrypt.generate_password_hash(registerForm.password.data).decode('utf-8')
        if hashedPass:
            userToAdd = users(registerForm.username.data, hashedPass)
            db.session.add(userToAdd)
            db.session.commit()
            flash("User created successfully", "Success")
            return redirect(url_for('authentication.login'))

def CheckIfUserIsAdmin():
    if current_user.isAdmin == False:
            flash("Can't register, unless you're an admin", 'Failed')
            return redirect(url_for('main.home'))