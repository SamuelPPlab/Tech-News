from tech_news.database import search_news
from datetime import datetime


def convert_to_tupla(list):
    return [(item['title'], item['url']) for item in list]


# Requisito 6
def search_by_title(title):
    search = search_news({'title': {'$regex': title, '$options': 'i'}})
    return convert_to_tupla(search)


# Requisito 7
def search_by_date(date):
    format_to_check = '%Y-%m-%d'
    try:
        datetime.strptime(date, format_to_check)
        search = search_news({'timestamp': {'$regex': date, '$options': 'i'}})
        return convert_to_tupla(search)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    search = search_news({'sources': {'$regex': source, '$options': 'i'}})
    return convert_to_tupla(search)


# Requisito 9
def search_by_category(category):
    search = search_news({'categories': {'$regex': category, '$options': 'i'}})
    return convert_to_tupla(search)
