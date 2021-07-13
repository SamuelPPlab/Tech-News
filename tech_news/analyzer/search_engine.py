from tech_news.database import search_news
# from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    result = search_news({'title': {'$regex': title, '$options': 'i'}})
    list = []
    for x in result:
        touple = (x['title'], x['url'])
        list.append(touple)
    return list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    result = search_news({'sources': {'$elemMatch': {
        '$regex': source, '$options': 'i'}}})
    list = []
    for x in result:
        touple = (x['title'], x['url'])
        list.append(touple)
    return list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    result = search_news({'categories': {'$elemMatch': {
        '$regex': category, '$options': 'i'}}})
    list = []
    for x in result:
        touple = (x['title'], x['url'])
        list.append(touple)
    return list