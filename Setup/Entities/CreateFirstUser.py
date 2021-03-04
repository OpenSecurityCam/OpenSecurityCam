import sys
sys.path.append('..')

from WebPortal import db, bcrypt, create_WebPortal
from WebPortal.models import users



app = create_WebPortal()
app.app_context().push()

print("Setting up the first user")
username = input("Username: ")
password = input("Password: ")

try:
    db.create_all(app=create_WebPortal())

    hashedPass = bcrypt.generate_password_hash(f"{password}")
    user = users(f"{username}", hashedPass, 1)

    db.session.add(user)
    db.session.commit()
except:
    print('User already created!')
