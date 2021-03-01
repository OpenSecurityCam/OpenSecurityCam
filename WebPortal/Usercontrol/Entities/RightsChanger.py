from WebPortal import db
from WebPortal.models import users

from flask_login import current_user
from flask.helpers import flash, url_for
from werkzeug.utils import redirect

class RightsChangerClass:
    # Constructor
    def __init__(self, username):
        self.username = username

    # Main Fuction
    def Main(self):
        # Checks if the current user is an admin
        if current_user.isAdmin:
            # Checks if the user exists
            if self.__User():
                # Checks the user's rights
                if self.__User().isAdmin == False:
                    return self.__ChangeToAdmin(self.__User())
                else:
                    return self.__ChangeToNormal(self.__User())
            else:
                return self.__FlashUserNotFound()
        else:
            self.__FlashUserNotAdmin()

    # Finds the user giving user string 
    def __User(self):
        return users.query.filter_by(username = self.username).first()

    # Changes the user rights to admin
    def __ChangeToAdmin(self, foundUser):
        foundUser.isAdmin = True;
        db.session.commit()
        flash(f'{foundUser.username} is now an admin.', 'Success')
        return redirect(url_for('UserControl.AdminPanel'))

    # Changes the user rights to regular
    def __ChangeToNormal(self, foundUser):
        foundUser.isAdmin = False;
        db.session.commit()
        flash(f'{foundUser.username} is not an admin anymore.', 'Success')
        return redirect(url_for('UserControl.AdminPanel'))

    # Flashed a message and redirects to the AdminPanel page if the user isn't found
    def __FlashUserNotFound():
        flash('User not found', 'Failed')
        return redirect(url_for('UserControl.AdminPanel'))

    # Flashes a message and redirects to the Userinfo page if the current user isn't admin
    def __FlashUserNotAdmin():
        flash('You need to be an admin to do this operation', 'Failed')
        return redirect(url_for('UserControl.Userinfo'))