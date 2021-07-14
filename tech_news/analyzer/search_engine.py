from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    # Bloco 24 - MongoDB: Updates Simples e Complexos - regex
    get_news = search_news({"title": {"$regex": title, "$options": "i"}})
    title_and_url = []
    for news in get_news:
        title_and_url.insert(len(title_and_url), (news["title"], news["url"]))
    return title_and_url


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
