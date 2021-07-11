import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    newsByTitle = search_news({"title": {"$regex": title, "$options": "i"}})
    newsList = []
    for news in newsByTitle:
        newsList.append((news['title'], news['url']))
    return newsList


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        newsByDate = search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")

    newsList = []
    for news in newsByDate:
        newsList.append((news['title'], news['url']))
    return newsList


# Requisito 8
def search_by_source(source):
    try:
        newsBySource = search_news({
            "sources": {"$regex": source, "$options": "i"}})
    except ValueError:
        raise ValueError("Fonte inválida")

    newsList = []
    for news in newsBySource:
        newsList.append((news['title'], news['url']))
    return newsList


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
