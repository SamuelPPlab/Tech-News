from tech_news.database import search_news
import datetime

regex = datetime.datetime.strptime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    get_news_titles = search_news(query)
    news_list = []
    for news in get_news_titles:
        new = (news["title"], news["url"])
        news_list.append(new)
    return news_list


# src: https://stackoverflow.com/questions/9978534
# /match-dates-using-python-regular-expressions/9978804


def valid_date(datestring):
    try:
        datetime.datetime.strptime(datestring, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_date(date):
    valid_date(date)
    query = {"timestamp": {"$regex": date}}
    get_news = search_news(query)
    news_list = []
    for news in get_news:
        new = (news["title"], news["url"])
        news_list.append(new)
    return news_list


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": source, "$options": "i"}}
    get_news = search_news(query)
    news_list = []
    for news in get_news:
        new = (news["title"], news["url"])
        news_list.append(new)
    return news_list


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": category, "$options": "i"}}
    get_news = search_news(query)
    news_list = []
    for news in get_news:
        new = (news["title"], news["url"])
        news_list.append(new)
    return news_list
