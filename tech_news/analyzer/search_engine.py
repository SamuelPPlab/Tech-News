from tech_news.database import search_news
from datetime import datetime


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
# Referência:
# https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, '%Y-%m-%d')
        result = search_news({"timestamp": {"$regex": date}})
        list = []
        for x in result:
            touple = (x['title'], x['url'])
            list.append(touple)
        return list
    except ValueError:
        raise ValueError("Data inválida")


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
