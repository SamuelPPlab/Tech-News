from tech_news.database import search_news


def search_by_title(title):
    titles_results = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(title["title"], title["url"]) for title in titles_results]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
