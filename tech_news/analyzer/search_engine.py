import re
from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    title_formated = re.compile(re.escape(title), re.IGNORECASE)
    responses = search_news({"title": title_formated})
    list = []
    for response in responses:
        list.append((response["title"], response["url"]))
    return list


# Requisito 7
def search_by_date(date):
    try:
        date != datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        date_formated = re.compile(re.escape(date), re.IGNORECASE)
        responses = search_news({"timestamp": date_formated})
        list = []
        for response in responses:
            list.append((response["title"], response["url"]))
    return list


# Requisito 8
def search_by_source(source):
    source_formated = re.compile(re.escape(source), re.IGNORECASE)
    responses = search_news({"sources": source_formated})
    list = []
    for response in responses:
        list.append((response["title"], response["url"]))
    return list


# Requisito 9
def search_by_category(category):
    category_formated = re.compile(re.escape(category), re.IGNORECASE)
    responses = search_news({"categories": category_formated})
    list = []
    for response in responses:
        list.append((response["title"], response["url"]))
    return list
