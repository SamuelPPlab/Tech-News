# Requisito 6
from tech_news.database import search_news, get_collection
import re
from datetime import datetime


def search_by_title(title):
    find_query = {"title": {"$regex": title, "$options": "i"}}
    news_search = search_news(find_query)
    news_list = []
    for news in news_search:
        news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news_db = get_collection().find(
            {"timestamp": {"$regex": re.compile(date)}},
            {"_id": 0, "title": 1, "url": 1},
        )
        news_list = []
        for news in news_db:
            news_list.append((news["title"], news["url"]))
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    find_query = {"sources": {"$regex": source, "$options": "i"}}
    news_search = search_news(find_query)
    news_list = []
    for news in news_search:
        news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 9
def search_by_category(category):
    find_query = {"categories": {"$regex": category, "$options": "i"}}
    news_search = search_news(find_query)
    news_list = []
    for news in news_search:
        news_list.append((news["title"], news["url"]))
    return news_list
