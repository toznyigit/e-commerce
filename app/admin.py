import json
from flask import Blueprint, render_template, make_response, jsonify, flash, redirect, request, url_for
from flask_login import login_required, current_user
from functools import wraps
from .database_connector import CommentDB, ItemDB, UserDB

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

@admin.post('/create_user')
@login_required
@authorization_required
def create_user():
    new_user = request.form.to_dict()
    new_user['type'] = 0

    if not new_user['name']:
        flash('You can not create empty user!','error')
    elif UserDB().read(name=new_user['name']):
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
        CommentDB().deleteAll(user=request.form['name'])
    return redirect(url_for('admin.panel'))

@admin.post('/create_item')
@login_required
@authorization_required
def create_item():
    new_item = request.form.to_dict()
    if not new_item['name']:
        flash('You can not create empty item!','error')
    elif ItemDB().read(name=new_item['name']):
        flash(f'{new_item["name"]} already exists!','error')
    else:
        ItemDB().create(**new_item)
    return redirect(url_for('admin.panel'))

@admin.post('/delete_item')
@login_required
@authorization_required
def delete_item():
    ItemDB().delete(name=request.form['name'])
    CommentDB().deleteAll(item=request.form['name'])
    return redirect(url_for('admin.panel'))