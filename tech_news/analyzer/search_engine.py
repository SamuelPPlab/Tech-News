from tech_news.database import search_news
from datetime import datetime
# Requisito 6


def search_by_title(title):
    query_search = {'title': {'$regex': title, '$options': 'i'}}
    news_by_title = search_news(query_search)
    news_all = []
    for news in news_by_title:
        title = news.get("title")
        url = news.get("url")
        news_all.append((title, url))
    return news_all


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")

    query_search = {
        "timestamp": {
            "$gte": date+"T00:00:00",
            "$lte": date+"T23:59:59",
        }
    }
    news_by_title = search_news(query_search)
    news_all = []
    for news in news_by_title:
        title = news.get("title")
        url = news.get("url")
        news_all.append((title, url))
    return news_all


# Requisito 8
def search_by_source(source):
    query_search = {"sources": {
        "$elemMatch": {"$regex": source, "$options": "i"}}
    }
    news_by_title = search_news(query_search)
    news_all = []
    for news in news_by_title:
        title = news.get("title")
        url = news.get("url")
        news_all.append((title, url))
    return news_all


# Requisito 9
def search_by_category(category):
    query_search = {"categories": {
        "$elemMatch": {"$regex": category, "$options": "i"}}
    }
    news_by_title = search_news(query_search)
    news_all = []
    for news in news_by_title:
        title = news.get("title")
        url = news.get("url")
        news_all.append((title, url))
    return news_all
