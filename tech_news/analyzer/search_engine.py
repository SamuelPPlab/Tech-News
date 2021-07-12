# import re
import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    searched_news = search_news({'title': {'$regex': title, '$options': 'i'}})
    news = []
    for searched_new in searched_news:
        news.append((searched_new["title"], searched_new["url"]))
    return news


# Requisito 7
def search_by_date(date):
    # https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
    # https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        searched_by_date = search_news({"timestamp": {'$regex': date}})
    except ValueError:
        raise ValueError("Data inválida")
    news = []
    for new in searched_by_date:
        news.append((new['title'], new['url']))
    return news
    #         news = []
    #         for new in searched_by_date:
    #             news.append((new["title"], new["url"]))
    #             return news
    # try:
    #     regex = r"^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$"
    #     if re.match(regex, date) is not None:
    #         searched_by_date = search_news({"timestamp": {'$regex': date}})
    #     else:
    #         return []
    # except ValueError:
    #     raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
