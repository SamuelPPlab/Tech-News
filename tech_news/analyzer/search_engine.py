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
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
