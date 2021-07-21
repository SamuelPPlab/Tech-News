from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Busca por titulo do Banco de dados"""
    search = {"title": {"$regex": title, "$options": "i"}}
    result = search_news(search)
    return [(news["title"], news["url"]) for news in result]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
