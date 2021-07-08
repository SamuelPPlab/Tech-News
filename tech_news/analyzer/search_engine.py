from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    rgx = re.compile(f'.*{title}.*', re.IGNORECASE)
    results = search_news({"title": rgx})
    news = []
    for result in results:
        a = (result["title"], result["url"])
        news.append(a)
    return news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
