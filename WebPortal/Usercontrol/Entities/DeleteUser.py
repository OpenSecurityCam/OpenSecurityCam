from WebPortal import db
from WebPortal.models import users

from flask_login import current_user
from flask.helpers import flash, url_for
from werkzeug.utils import redirect


class DeleteUserClass:
    # Constructor
    def __init__(self, username):
        self.username = username

    def Main(self):
        # Checks if the user is an admin`
        if current_user.isAdmin:
            # checks if the user exists in the db
            if self.__CurrentUser():
                return self.__DeleteUser(self.__CurrentUser())
            else:
                return self.__FlashUserNotFound()
        else:
            return self.__FlashUserNotAdmin()
    
    # Finds the user giving user string 
    def __CurrentUser(self):
        return users.query.filter_by(username = self.username).first()

 
    # Deletes the given user
    def __DeleteUser(self, foundUser):
        db.session.delete(foundUser)
        db.session.commit()
        flash(f'{foundUser.username} deleted successfully.', 'Success')
        return redirect(url_for('UserControl.AdminPanel'))

    # Flashes a message and redirects to the AdminPanel page if the user isn't found
    def __FlashUserNotFound():
        flash('User not found', 'Failed')
        return redirect(url_for('UserControl.AdminPanel'))
    
    # Flashes a message and redirects to the Userinfo page if the current user isn't an admin
    def __FlashUserNotAdmin():
        flash('You need to be an admin to do this operation', 'Failed')
        return redirect(url_for('UserControl.Userinfo'))
