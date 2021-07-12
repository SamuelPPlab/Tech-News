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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
