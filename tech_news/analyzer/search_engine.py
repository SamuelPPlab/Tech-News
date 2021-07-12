from tech_news.database import search_news

#referência: Andre Horman
def insensitive(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    return query


# Requisito 6
def search_by_title(title):
    titles = []
    query = insensitive(title)
    response_list = search_news(query)
    for news in response_list:
        titles.append((news["title"], news["url"]))

    return titles


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
