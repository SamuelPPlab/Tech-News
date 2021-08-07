# Requisito 6
from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""

    get_news = search_news({"title": {"$regex": title, "$options": "i"}})
    info = list()
    for news_item in get_news:
        if news_item["title"]:
            get_tuple = (news_item["title"], news_item["url"])
            info.append(get_tuple)
    return info


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        info = list()
        news = search_news({"timestamp": {"$regex": date}})
        for news_item in news:
            get_tuple = (news_item["title"], news_item["url"])
            info.append(get_tuple)
        return info


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
