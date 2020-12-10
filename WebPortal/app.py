from flask import Flask, render_template, request, redirect, url_for, session, flash
from entities.flashes import Flashes as flashMSG
# from entities.tableModel import User as u
import flask_sqlalchemy as sqlachemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/LibreSecurityCam'

db = sqlachemy.SQLAlchemy(app)

app.secret_key = "iuklsdfl08708"

class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True, nullable = False)
    username = db.Column("username", db.String(50), nullable = False)
    passcode = db.Column("passcode", db.Integer, nullable = False)
    _isAdmin = db.Column("isAdmin", db.Boolean, nullable = False, default = False)

    def __init__(self, username, passcode):
        self.username = username
        self.passcode = passcode

@app.route('/', methods=['GET'])
def Main():
    if 'user' in session:
        return render_template('html/index.html', userInfo = session['user'])
    else:
        return render_template('html/index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        passcodeForm = request.form['passcode']
        if passcodeForm == request.form['repeatPasscode']:
            foundUser = User.query.filter_by(passcode = passcodeForm).first()
            if foundUser:
                flash("Can't create user with the same credentials")
                return redirect(url_for('register'))
            else:
                session['user'] = username
                user = User(username, passcodeForm)
                print(f"{user.username} {user.passcode}")
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('Main'))
        else:
            flashMSG.PassNotMatch()
            return redirect(url_for('register'))
    else:
        if 'user' in session:
            flashMSG.AlreadyLoggedIn()
            return redirect(url_for("Main"))
        return render_template('html/register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        foundUser = User.query.filter_by(passcode = request.form['passcode']).first()
        if foundUser:
            session['user'] = foundUser.username
            flashMSG.LoginSuccessful()
            return redirect(url_for("Main"))
        else: 
            flashMSG.WrongPasscode()
            return redirect(url_for('login'))
    else:
        if 'user' in session:
            flashMSG.AlreadyLoggedIn()
            return redirect(url_for("Main"))
        return render_template('html/login.html')

@app.route('/userinfo', methods=['GET', 'POST'])
def userinfo():
    if 'user' in session:
        if request.method == 'POST':
            usernameForm = request.form['username']
            passcodeForm = request.form['currentPasscode'] 
            newPasscodeForm = request.form['newPasscode']
            if usernameForm and passcodeForm == newPasscodeForm:
                foundUser = User.query.filter_by(passcode = passcodeForm).first()
                if foundUser:
                    foundUser.username = usernameForm
                    db.session.commit()
                    session['user'] = foundUser.username
                    flashMSG.CredentialChanged()
                    return redirect(url_for('userinfo'))
                else:
                    flashMSG.WrongPasscode()
                    return redirect(url_for('userinfo'))
            elif passcodeForm != newPasscodeForm:
                foundUser = User.query.filter_by(passcode = passcodeForm).first()
                if foundUser:
                    pass
            else:
                return "Error"
        else:
            return render_template('html/userinfo.html', userInfo = session['user'])
    else:
        flashMSG.HaventLoggedIn()
        return redirect(url_for("login"))
    
@app.route('/logout')
def logout():
    if session:
        session.clear()
        flashMSG.LoggedOut()
    else:
        flashMSG.NotLoggedIn()
    return redirect(url_for('Main'))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)