import re
import datetime
from tech_news.database import db


# Requisito 6
def search_by_title(title):
    list_news = []
    for new in db.news.find({"title": re.compile(title, re.IGNORECASE)}):
        new_item = (new['title'], new['url'])
        list_news.append(new_item)
    return list_news


# Requisito 7
def search_by_date(date):
    list_news_for_date = []
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        for new in db.news.find({"timestamp": {"$regex": date}}):
            new_item = (new['title'], new['url'])
            list_news_for_date.append(new_item)
    except ValueError:
        raise ValueError('Data inválida')
    else:
        return list_news_for_date


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
