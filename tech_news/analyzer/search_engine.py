# Requisito 6
from tech_news.database import search_news
import re


def search_by_title(title):
    def search_by_title(title):
        rgx = re.compile(f".*{title}.*", re.IGNORECASE)
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
    news = []
    rgx = re.compile(category, re.IGNORECASE)
    results = search_news({"categories": rgx})
    for result in results:
        news_tupla = (result["title"], result["url"])
        news.append(news_tupla)
    return news
