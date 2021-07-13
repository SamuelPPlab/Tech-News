from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news = search_news({"timestamp": {"$regex": date}})
        return [(new["title"], new["url"]) for new in news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news = search_news({"categories": {"$regex": category, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]
