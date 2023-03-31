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
    return render_template('panel.html', user_table=UserDB().readAll(), popup=False)

@admin.get('/create_user')
@login_required
@authorization_required
def create_user_popup():
    return render_template('panel.html', user_table=UserDB().readAll(), popup=True)

@admin.post('/create_user')
@login_required
@authorization_required
def create_user():
    new_user = request.form.to_dict()
    new_user['type'] = 0
    if UserDB().read(name=new_user['name']):
        flash(f'{new_user["name"]} already exists!','error')
    else:
        UserDB().create(**new_user)
    return redirect(url_for('admin.panel'))

@admin.post('/delete_user')
@login_required
@authorization_required
def delete_user():
    target_name = request.form['name']
    if current_user._user.username == target_name:
        flash('You can not delete yourself!','error')
    else:
        UserDB().delete(name=request.form['name'])
    return redirect(url_for('admin.panel'))
