from flask import Flask, render_template, request, redirect, url_for, session, flash
from entities.flashes import Flashes as flashMSG
import sqlalchemy
app = Flask(__name__)
app.secret_key = "iuklsdfl08708"

@app.route('/', methods=['GET'])
def Main():
    if 'user' in session:
        return render_template('html/index.html', userInfo = session['user'])
    else:
        return render_template('html/index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['name']
        flashMSG.LoginSuccessful()
        return redirect(url_for("Main"))
    else:
        if 'user' in session:
            flashMSG.AlreadyLoggedIn()
            return redirect(url_for("Main"))
        return render_template('html/login.html')

@app.route('/userinfo', methods=['GET', 'POST'])
def userinfo():
    if 'user' in session:
        if request.method == 'POST':
            session['user'] = request.form['name']
            flashMSG.NameChanged()
            return render_template('html/userinfo.html', userInfo = session['user'])
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