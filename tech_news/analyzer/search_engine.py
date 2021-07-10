import tech_news.database as db
import re
from datetime import datetime


def get_tuple_list(news_list):
    return list(map(lambda news: (news["title"], news["url"]), news_list))


def check_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 6


def search_by_title(title):
    news_list = db.search_news(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    )
    news_tuple_list = get_tuple_list(news_list)
    return news_tuple_list


# Requisito 7
def search_by_date(date):
    check_date(date)
    news_list = db.search_news({"timestamp": {"$regex": date}})
    return get_tuple_list(news_list)


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
