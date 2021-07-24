# Requisito 6
from tech_news.database import find_news


def search_by_title(title):

    list_news = find_news()

    return [
        (news["title"], news["url"])
        for news in list_news if title.lower() in news["title"].lower()
    ]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
