from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    newsletter = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(item["title"], item["url"]) for item in newsletter]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        newsletter = search_news({"timestamp": {"$regex": date}})
        return [(item["title"], item["url"]) for item in newsletter]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    newsletter = search_news({"sources": {"$regex": source, "$options": "i"}})
    return [(item["title"], item["url"]) for item in newsletter]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
