from flask.helpers import flash, url_for
from flask.templating import render_template
from flask_login.utils import login_user
from werkzeug.utils import redirect
from flask_login import current_user

from WebPortal import db, bcrypt
from WebPortal.models import users

def RegisterUser(registerForm):
    if registerForm.validate_on_submit():
        try:
            hashedPass = bcrypt.generate_password_hash(registerForm.password.data).decode('utf-8')
            userToAdd = users(registerForm.username.data, hashedPass)
            db.session.add(userToAdd)
            db.session.commit()
            flash("User created successfully", "Success")
            login_user(userToAdd)
            return redirect(url_for('usercontrol.userinfo'))
        except:
            flash("Something went wrong with the registration", 'Failed')
    return render_template('register.html', form = registerForm)

def CheckIfUserIsAdmin():
    if current_user.isAdmin == False:
            flash("Can't register, unless you're an admin", 'Failed')