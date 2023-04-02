from datetime import datetime
from .database_connector import ItemDB, CommentDB

def fancy_date_mapper(comment):
    comment_timestap = comment['datetime']
    now = datetime.now().timestamp()
    diff = int(now-float(comment_timestap))
    if diff < 59:
        comment['datetime'] = f'{diff}s'
    elif 60 < diff < 3599:
        comment['datetime'] = f'{diff//60}m'
    elif 3600 < diff < 86399:
        comment['datetime'] = f'{diff//3600}h'
    elif 86400 < diff < 2591999:
        comment['datetime'] = f'{diff//86400}d'
    else:
        comment['datetime'] = f'{diff//259200}M'

    return comment

def average_score(item):
    _comments = CommentDB().readAllbyItem(item=item['name'])
    rating = round(sum(map(lambda x: int(x['rating']), _comments))/len(_comments)*1.0, 2) if _comments else 0.0
    item['rating'] = str(rating)
    return item