import secrets
from PIL import Image
import os


from flask.helpers import url_for, flash
from flask.templating import render_template
from werkzeug.utils import redirect
from WebPortal.models import users
from flask.globals import request

from WebPortal import db
from WebPortal.Usercontrol.Forms.ChangeProfilePicForm import ChangeProfilePictureForm

class ProfilePictureChangerClass:
    # Constructor
    def __init__(self, user):
        self.user = user

    # Main Function
    def Main(self):
        cppf = ChangeProfilePictureForm()
        if request.method == 'POST':
            self.__RemoveProfilePictureIfNotDefault()
            if cppf.profilePicture.data:
                try:
                    return self.__ChangeProfilePicture(cppf.profilePicture.data)
                except:
                    flash('The image was not in a correct format', 'Failed')
                    return redirect(url_for('UserControl.AdminPanel'))

            else:
                return self.__ChangeProfilePictureToDefault()
        else:
            return render_template('UpdateProfilePicture.html', form = cppf, userProfilePicture=self.__User().profilePicture)
    
    
    # Find the given user
    def __User(self):
        return users.query.filter_by(username = self.user).first()

    # Remove the profile picture if it isn't the default one
    def __RemoveProfilePictureIfNotDefault(self):
        if self.__User().profilePicture != 'default.png':
            try:
                os.remove('WebPortal/static/profilePics/' + self.__User().profilePicture)
            except:
                return self.__ChangeProfilePictureToDefault()

    # Change the profile picture
    def __ChangeProfilePicture(self, profilePicture):
        self.__User().profilePicture = self.__save_picture(profilePicture)
        db.session.commit()
        return redirect(url_for('UserControl.AdminPanel'))

    # Change the profile picture to the default one
    def __ChangeProfilePictureToDefault(self):
        self.__User().profilePicture = 'default.png'
        db.session.commit()
        return redirect(url_for('UserControl.AdminPanel'))

    # saves picture to the css/profilePics directory
    def __save_picture(self, picture):
        # generates a random hex 
        random_hex = secrets.token_hex(8)
        # gets the picture filename and splits the file extension and file name
        _, f_ext = os.path.splitext(picture.filename)
        # change file name
        picture_fn = random_hex + f_ext
        # give the path to save the picture to
        picture_path = os.path.join('WebPortal/static/profilePics', picture_fn)

        # resize the image to the size
        output_size = (300, 300)
        # save the image
        i = Image.open(picture)
        i.thumbnail(output_size)
        i.save(picture_path)

        # return the image so it can be used to be changed in the database
        return picture_fn

