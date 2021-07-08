import re
from tech_news.database import db


# Requisito 6
def search_by_title(title):
    list_news = []
    print(db.news.find({"title": {"$regex": title}}))
    for new in db.news.find({"title": re.compile(title, re.IGNORECASE)}):
        new_item = (new['title'], new['url'])
        list_news.append(new_item)
    return list_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
