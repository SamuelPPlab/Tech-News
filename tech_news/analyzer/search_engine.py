from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    search_results = search_news({"title": {"$regex": title, "$options": "i"}})
    list = []
    for result in search_results:
        list.append((result['title'], result['url']))

    return list


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        search_results = search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError('Data inválida')

    list = []
    for result in search_results:
        list.append((result['title'], result['url']))

    return list


# Requisito 8
def search_by_source(source):
    search_results = search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    list = []
    for result in search_results:
        list.append((result['title'], result['url']))

    return list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
