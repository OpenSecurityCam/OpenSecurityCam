from app import app
from WebPortal import db, bcrypt, create_WebPortal
from WebPortal.models import users

app = create_WebPortal()
app.app_context().push()

db.create_all(app=create_WebPortal())

hashedPass = bcrypt.generate_password_hash("root123")
user = users("Admin", hashedPass, 1)

db.session.add(user)
db.session.commit()
