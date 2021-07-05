import re
from tech_news.database import search_news


def format_document(dict):
    return (dict['title'], dict['url'])


# Requisito 6
def search_by_title(title):
    results = search_news({'title': {'$regex': title, '$options': 'i'}})
    return [format_document(news) for news in results]


# Requisito 7
def search_by_date(date):
    date_regex = r'^20\d{2}-(0[1-9]|1[0-2])-(0[1-9]|1\d|2\d|3[01])$'
    if (re.search(date_regex, date) is None):
        raise ValueError("Data inválida")

    results = search_news({'timestamp': {'$regex': date}})
    return [format_document(news) for news in results]


# Requisito 8
def search_by_source(source):
    results = search_news({'sources': {'$regex': source, '$options': 'i'}})
    return [format_document(news) for news in results]


# Requisito 9
def search_by_category(category):
    results = search_news(
        {'categories': {'$regex': category, '$options': 'i'}}
    )
    return [format_document(news) for news in results]
