from flask.helpers import flash, url_for
from flask.templating import render_template
from flask_login import login_user, current_user
from werkzeug.utils import redirect

from WebPortal import db, bcrypt
from WebPortal.models import users
from WebPortal.authentication.forms import RegisterForm

class Registrator:
    def RegisterUser(self):
        registerForm = RegisterForm()
        if current_user.isAdmin:
            try:
                self.__RegisterTheUser(registerForm)
            except:
                flash("Something went wrong with the registration", 'Failed')
        else:
            return redirect(url_for('main.home'))
            flash("You can't register a user, unless you're an admin", 'Failed')
        return render_template('register.html', form = registerForm)

    def __RegisterTheUser(self, registerForm):
        if registerForm.validate_on_submit():
            registerForm = RegisterForm()
            hashedPass = bcrypt.generate_password_hash(registerForm.password.data).decode('utf-8')
            userToAdd = users(registerForm.username.data, hashedPass)
            db.session.add(userToAdd)
            db.session.commit()
            flash("User created successfully", "Success")
            login_user(userToAdd)
            return redirect(url_for('usercontrol.userinfo'))