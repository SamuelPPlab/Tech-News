from tech_news.database import search_news, find_news
import datetime


# Requisito 6
def search_by_title(title):
    allNews = find_news()
    tuple = []
    for news in allNews:
        if news["title"].lower() == title.lower():
            tuple.append((news["title"], news["url"]))
    return tuple


""" REF:
https://stackoverflow.com/questions/4709652/python-regex-to-match-dates 
"""


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    allNews = search_news({"timestamp": {"$regex": f"{date}"}})
    tuple = []
    for news in allNews:
        tuple.append((news["title"], news["url"]))
    return tuple


# Requisito 8
def search_by_source(source):
    allNews = find_news()
    tuple = []
    for news in allNews:
        for s in news["sources"]:
            if s.lower() == source.lower():
                tuple.append((news["title"], news["url"]))
    return tuple


# Requisito 9
def search_by_category(category):
    allNews = find_news()
    tuple = []
    for news in allNews:
        for cat in news["categories"]:
            if cat.lower() == category.lower():
                tuple.append((news["title"], news["url"]))
    return tuple
