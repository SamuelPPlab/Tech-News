from tech_news.database import search_news
from datetime import datetime


def format_news(new):
    return ((new["title"], new["url"]))


# Requisito 6
def search_by_title(title):
    news = []
    # https://docs.mongodb.com/manual/reference/operator/query/regex/
    search = {"title": {"$regex": title, "$options": "i"}}
    result = search_news(search)
    for new in result:
        news.append(format_news(new))
    return news


# Requisito 7
def search_by_date(date):
    news = []
    format = "%Y-%m-%d"
    try:
        # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
        datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")
    search = {"timestamp": {"$regex": date}}
    result = search_news(search)
    for new in result:
        news.append(format_news(new))
    return news


# Requisito 8
def search_by_source(source):
    news = []
    search = {"sources": {"$regex": source, "$options": "i"}}
    result = search_news(search)
    for new in result:
        news.append(format_news(new))
    return news


# Requisito 9
def search_by_category(category):
    news = []
    search = {"categories": {"$regex": category, "$options": "i"}}
    result = search_news(search)
    for new in result:
        news.append(format_news(new))
    return news
