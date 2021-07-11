import datetime

from tech_news.database import (
    search_news,
)


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": f"{title}", "$options": "i"}}
    lista = search_news(query)
    return [(news["title"], news["url"]) for news in lista]


# Requisito 7
def search_by_date(date):
    format = "%Y-%m-%d"
    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")
    else:
        query = {"timestamp": {"$regex": f"{date}", "$options": "i"}}
        lista = search_news(query)
        return [(news["title"], news["url"]) for news in lista]


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": f"{source}", "$options": "i"}}
    lista = search_news(query)
    return [(news["title"], news["url"]) for news in lista]


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": f"{category}", "$options": "i"}}
    lista = search_news(query)
    return [(news["title"], news["url"]) for news in lista]
