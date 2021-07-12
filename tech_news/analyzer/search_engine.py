from datetime import datetime

from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    search = search_news(query)
    list = []
    for news in search:
        list.append((news["title"], news["url"]))
    return list


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        query = {"timestamp": {"$regex": date}}
        search = search_news(query)
        list = []
        for news in search:
            list = [(news["title"], news["url"])]
        return list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
