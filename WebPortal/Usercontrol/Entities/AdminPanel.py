from WebPortal.models import users

from flask.helpers import url_for
from flask.templating import render_template
from flask_login import current_user
from werkzeug.utils import redirect

class AdminPanelClass:
    def AdminPanel():
        # Checks if the current user is an admin
        if current_user.isAdmin:
            userList = users.query.all()
            return render_template('AdminPanel.html', Users = userList)
        else:
            # Redirects to the Userinfo page if it isn't admin
            return redirect(url_for('UserControl.Userinfo'))
