from tech_news.database import search_news
import re
import datetime


# Requisito 6
def search_by_title(title):
    rgx = re.compile(f".*{title}.*", re.IGNORECASE)

    results = search_news({"title": rgx})
    news = []
    for result in results:
        tupla = (result["title"], result["url"])
        news.append(tupla)
    return news


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        rgx = re.compile(f".*{date}.*")
        results = search_news({"timestamp": rgx})
        news = []
        for result in results:
            tupla = (result["title"], result["url"])
            news.append(tupla)
    return news


# Requisito 8
def search_by_source(source):
    news = []
    for source_item in source:
        rgx = re.compile(f".*{source_item}.*", re.IGNORECASE)
        results = search_news({"sources": rgx})
        for result in results:
            tupla = (result["title"], result["url"])
            news.append(tupla)
        return news


# Requisito 9
def search_by_category(category):
    news = []
    rgx = re.compile(category, re.IGNORECASE)
    results = search_news({"categories": rgx})
    for result in results:
        news_tupla = (result["title"], result["url"])
        news.append(news_tupla)
    return news
