from tech_news.database import search_news
from datetime import datetime
# https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_data = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_data]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    format_date = "%Y-%m-%d"
    try:
        datetime.strptime(date, format_date)
        news_data = search_news({"timestamp": {"$regex": date}})
        return [(news["title"], news["url"]) for news in news_data]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news_data = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_data]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news_data = search_news(
        {"categories": {"$regex": category, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_data]
