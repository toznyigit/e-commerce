from datetime import datetime
from flask import Blueprint, redirect, render_template, request, make_response, url_for
from flask_login import login_required, current_user
from .database_connector import ItemDB, CommentDB
from .utils import average_score, fancy_date_mapper

main = Blueprint('main', __name__)

@main.get('/')
def index():
    try:
        return render_template('index.html', name=current_user._user.username, is_admin=current_user._user.type)
    except AttributeError:
        return render_template('index.html', name=None, is_admin=None)
    
@main.post('/get_item')
def get_item():
    if request.get_json()['category'] == 'All':
        _items = map(average_score, ItemDB().readAll())
    else:
        _items = map(average_score, ItemDB().readCat(**request.get_json()))
        
    return make_response(list(_items), 200)
    
@main.get('/item')
def page_item():
    _item = ItemDB().read(name=request.args['name'])
    _comments = CommentDB().readAllbyItem(item=request.args['name'])
    _comments = list(map(fancy_date_mapper, _comments))
    _item['rating'] = round(sum(map(lambda x: int(x['rating']), _comments))/len(_comments)*1.0, 2) if _comments else 0.0
    try:
        return render_template('item_page.html', 
                                    name=current_user._user.username, 
                                    is_admin=current_user._user.type, 
                                    item=_item,
                                    comments=_comments)
    except AttributeError:
        return render_template('item_page.html', 
                                    name=None,
                                    is_admin=None,
                                    item=_item,
                                    comments=_comments)

@main.post('/comment')
@login_required
def post_comment():
    comment = {
        'user': current_user._user.username,
        'datetime': datetime.now().timestamp(),
    }
    comment.update(**request.get_json())
    if CommentDB().read(item=request.get_json()['item'],user= current_user._user.username):
        CommentDB().delete(item=request.get_json()['item'],user= current_user._user.username)
    CommentDB().create(**comment)
    return make_response({}, 200)

@main.post('/delete_comment')
@login_required
def delete_comment():
    CommentDB().delete(**request.form.to_dict())
    return redirect(url_for('main.profile'))

@main.get('/profile')
@login_required
def profile():
    _comments = CommentDB().readAllbyUser(user=current_user._user.username)
    _comments = list(map(fancy_date_mapper, _comments))
    rating = round(sum(map(lambda x: int(x['rating']), _comments))/len(_comments)*1.0, 2) if _comments else 0.0
    return render_template('profile.html', 
                                name=current_user._user.username, 
                                is_admin=current_user._user.type, 
                                rating=rating, 
                                comments=_comments)
    