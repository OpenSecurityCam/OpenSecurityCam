from flask import Blueprint, redirect, url_for, render_template

from flask_login import current_user

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('authentication.login'))
