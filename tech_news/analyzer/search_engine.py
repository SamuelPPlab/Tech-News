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


def search_off_case_sensitive(key, search):
    return db.search_news({key: {"$regex": re.compile(search, re.IGNORECASE)}})


# Requisito 6


def search_by_title(title):
    news_list = search_off_case_sensitive("title", title)
    news_tuple_list = get_tuple_list(news_list)
    return news_tuple_list


# Requisito 7
def search_by_date(date):
    check_date(date)
    news_list = search_off_case_sensitive("timestamp", date)
    return get_tuple_list(news_list)


# Requisito 8
def search_by_source(source):
    news_list = search_off_case_sensitive("sources", source)
    return get_tuple_list(news_list)


# Requisito 9
def search_by_category(category):
    news_list = search_off_case_sensitive("categories", category)
    return get_tuple_list(news_list)
