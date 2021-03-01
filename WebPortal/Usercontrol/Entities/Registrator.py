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
        # Intializes the register form
        registerForm = RegisterForm()
        if registerForm.validate_on_submit():
            if current_user.isAdmin:
                try:
                    return self.__RegisterTheUser(registerForm)
                except:
                    flash("Something went wrong with the registration", 'Failed')
            else:
                return self.__FlashUserNotAdmin()
        else:
            return render_template('register.html', form = registerForm)

    # Registers the user
    def __RegisterTheUser(self, registerForm):
        # Hashes the password 
        hashedPass = bcrypt.generate_password_hash(registerForm.password.data).decode('utf-8')
        # Adds user to database as a object 
        userToAdd = users(registerForm.username.data, hashedPass, 0)
        db.session.add(userToAdd)
        db.session.commit()
        flash("User created successfully", "Success")
        return redirect(url_for('UserControl.AdminPanel'))

    # Flashes a message and redirects to the Userinfo page if the current user isn't an admin
    def __FlashUserNotAdmin():
        flash('You need to be an admin to do this operation', 'Failed')
        return redirect(url_for('UserControl.Userinfo'))