from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    requested_news = search_news({"title": {"$regex": title, "$options": "i"}})
    if len(requested_news) > 0:
        return [(requested_news[0]["title"], requested_news[0]["url"])]
    else:
        return []


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news_by_date = search_news({"timestamp": {"$regex": date}})
        if len(news_by_date) > 0:
            return [(news_by_date[0]["title"], news_by_date[0]["url"])]
        else:
            return []
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news_by_source = search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    if len(news_by_source) > 0:
        return [(news_by_source[0]["title"], news_by_source[0]["url"])]
    else:
        return []


# Requisito 9
def search_by_category(category):
    news_by_category = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    if len(news_by_category) > 0:
        return [(news_by_category[0]["title"], news_by_category[0]["url"])]
    else:
        return []
