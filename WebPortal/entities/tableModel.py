import flask_sqlalchemy as sqlachemy

class InitDB:
    def __init__(self, app):
        self._app = app
    
    def InitDB(self):
        return sqlachemy.SQLAlchemy(_app)

db = InitDB.InitDB
