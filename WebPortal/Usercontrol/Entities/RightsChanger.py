from WebPortal import db
from WebPortal.models import users

from flask_login import current_user
from flask.helpers import flash, url_for
from werkzeug.utils import redirect

class RightsChangerClass:
    def __init__(self, username):
        self.username = username

    def __CurrentUser(self):
        return users.query.filter_by(username = self.username).first()

    def RightsChanger(self):
        if current_user.isAdmin:
            foundUser = self.__CurrentUser()
            if foundUser:
                if foundUser.isAdmin == False:
                    return self.__ChangeToAdmin(foundUser)
                else:
                    return self.__ChangeToNormal(foundUser)
            else:
                return self.__FlashUserNotFound()
        else:
            self.__FlashUserNotAdmin()

    def __ChangeToAdmin(self, foundUser):
        foundUser.isAdmin = True;
        db.session.commit()
        flash(f'{foundUser.username} is now an admin.', 'Success')
        return redirect(url_for('UserControl.AdminPanel'))

    def __ChangeToNormal(self, foundUser):
        foundUser.isAdmin = False;
        db.session.commit()
        flash(f'{foundUser.username} is not an admin anymore.', 'Success')
        return redirect(url_for('UserControl.AdminPanel'))

    def __FlashUserNotFound():
        flash('User not found', 'Failed')
        return redirect(url_for('UserControl.AdminPanel'))

    def __FlashUserNotAdmin():
        flash('You need to be an admin to do this operation', 'Failed')
        return redirect(url_for('UserControl.Userinfo'))