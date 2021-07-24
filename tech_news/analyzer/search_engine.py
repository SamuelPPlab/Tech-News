from tech_news.database import search_news


def search(key, value):
    query = search_news({key: {"$regex": f"{value}", "$options": "i"}})
    return [(news["title"], news["url"]) for news in query]


# Requisito 6
def search_by_title(title):
    return search("title", title)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    return search("sources", source)


# Requisito 9
def search_by_category(category):
    return search("categories", category)
