from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}

    data = search_news(query)

    noticias = []
    for news in data:
        title = news.get("title")
        url = news.get("url")
        noticias.append((title, url))
    return noticias


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    query = {"timestamp": {"$gte": date+"T00:00:00", "$lte": date+"T23:59:59"}}
    print(query)
    data = search_news(query)
    noticias = []
    for news in data:
        title = news.get("title")
        url = news.get("url")
        noticias.append((title, url))
    return noticias


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}}

    data = search_news(query)

    noticias = []
    for news in data:
        title = news.get("title")
        url = news.get("url")
        noticias.append((title, url))
    return noticias


# Requisito 9
def search_by_category(category):
    query = {
      "categories": {"$elemMatch": {"$regex": category, "$options": "i"}}
    }

    data = search_news(query)

    noticias = []
    for news in data:
        title = news.get("title")
        url = news.get("url")
        noticias.append((title, url))
    return noticias
