from flask import Blueprint, render_template, jsonify, flash, redirect, request, url_for
from flask_login import login_required, current_user
from functools import wraps
from .database_connector import UserDB

admin = Blueprint('admin', __name__)

def authorization_required(func):
    @wraps(func)
    def wrapper():
        if not current_user.is_admin:
            flash('You are not authorized!','error')
            return redirect(url_for('main.profile'))
        return func()
    return wrapper

@admin.get('/panel')
@login_required
@authorization_required
def panel():
    return render_template('panel.html', user_table=UserDB().readAll())

@admin.post('/delete_user')
@login_required
@authorization_required
def delete_user():
    UserDB().delete(name=request.form['name'])
    return redirect(url_for('admin.panel'))
