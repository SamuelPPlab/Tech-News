from tech_news.database import search_news


def format_document(dict):
    return (dict['title'], dict['url'])


# Requisito 6
def search_by_title(title):
    results = search_news({'title': {'$regex': title, '$options': 'i'}})
    return [format_document(news) for news in results]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
