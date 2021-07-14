from tech_news.database import search_news
import datetime


def insensitive(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    return query


# Requisito 6
def search_by_title(title):
    titles = []
    query = insensitive(title)
    response_list = search_news(query)
    for news in response_list:
        titles.append((news["title"], news["url"]))

    return titles


# Requisito 7
# https://stackoverflow.com/questions/4709652/python-regex-to-match-dates
def search_by_date(date):
    datetime.datetime.strptime(date, "%y-/%m-/%d")
    response_news_by_date = search_news({"timestamp": {"$regex": date}})

    if (response_news_by_date is None):
        raise ValueError("Data inválida")

    news = [(new['title'], new['url']) for new in response_news_by_date]
    return news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
