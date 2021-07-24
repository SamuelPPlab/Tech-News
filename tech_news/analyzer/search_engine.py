from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    result = list()
    query = search_news({"title": {"$regex": title, "$options": "i"}})
    for news in query:
        if news["title"]:
            format = (news["title"], news["url"])
            result.append(format)
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
