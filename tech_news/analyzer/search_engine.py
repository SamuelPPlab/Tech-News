from tech_news.database import search_news
import re

# Requisito 6


def search_by_title(title):
    # print(title) Vamoscomtudo
    pattern = re.compile(f'.*{title}.*', re.IGNORECASE)
    # print(pattern) VAMOSCOMTUDO
    results = search_news({"title": pattern})
    news = []
    for result in results:
        search = (result["title"], result["url"])
        news.append(search)
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
