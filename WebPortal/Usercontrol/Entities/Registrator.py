# Imports from Flask
from flask.helpers import flash, url_for
from flask.templating import render_template
from flask_login import login_user, current_user
from werkzeug.utils import redirect

# Imports from project
from WebPortal import db, bcrypt
from WebPortal.models import users
from WebPortal.Usercontrol.Forms.RegisterForm import RegisterForm

# Class that registers a user
class RegistratorClass:
    
    def RegisterUser(self):
        registerForm = RegisterForm()
        if registerForm.validate_on_submit():
            if current_user.isAdmin:
                try:
                    return self.__RegisterTheUser(registerForm)
                except:
                    flash("Something went wrong with the registration", 'Failed')
            else:
                flash("You can't register a user, unless you're an admin", 'Failed')
                return redirect(url_for('MainPage.Home'))
        else:
            return render_template('register.html', form = registerForm)

    def __RegisterTheUser(self, registerForm):
        hashedPass = bcrypt.generate_password_hash(registerForm.password.data).decode('utf-8')
        userToAdd = users(registerForm.username.data, hashedPass, 0)
        db.session.add(userToAdd)
        db.session.commit()
        flash("User created successfully", "Success")
        return redirect(url_for('UserControl.AdminPanel'))