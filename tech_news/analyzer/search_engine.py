# Requisito 6
from tech_news.database import find_news
from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):

    list_news = find_news()

    return [
        (news["title"], news["url"])
        for news in list_news if title.lower() in news["title"].lower()
    ]


# Requisito 7
def search_by_date(date):

    try:
        datetime.strptime(date, "%Y-%m-%d")
        news_list = search_news({"timestamp": {"$regex": date}})
        return [(news["title"], news["url"]) for news in news_list]

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
