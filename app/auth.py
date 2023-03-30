from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .database_connector import UserDB
from .auth_model import *

auth = Blueprint('auth', __name__)

@auth.get('/login')
def login():
    return render_template('login.html')

@auth.post('/login')
def login_post():
    username = request.form.get('username')
    passwd = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = UserDB().read(name=username, password=passwd)
    if not user:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(User(
        DBUser(user['name'], user['type'])
    ), remember=remember)
    return redirect(url_for('main.profile'))

@auth.get('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))