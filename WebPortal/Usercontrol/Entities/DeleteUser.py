from WebPortal import db
from WebPortal.models import users

from flask_login import current_user
from flask.helpers import flash, url_for
from werkzeug.utils import redirect


class DeleteUserClass:
    def __init__(self, username):
        self.username = username

    def __CurrentUser(self):
        return users.query.filter_by(username = self.username).first()

    def DeleteUser(self):
        if current_user.isAdmin:
            foundUser = self.__CurrentUser()
            if foundUser:
                return self.__CreateUserIfUserFound(foundUser)
            else:
                return self.__FlashUserNotFound()
        else:
            return self.__FlashUserNotAdmin()
 
    def __CreateUserIfUserFound(self, foundUser):
        db.session.delete(foundUser)
        db.session.commit()
        flash(f'{foundUser.username} deleted successfully.', 'Success')
        return redirect(url_for('UserControl.AdminPanel'))

    def __FlashUserNotFound():
        flash('User not found', 'Failed')
        return redirect(url_for('UserControl.AdminPanel'))

    def __FlashUserNotAdmin():
        flash('You need to be an admin to do this operation', 'Failed')
        return redirect(url_for('UserControl.Userinfo'))
