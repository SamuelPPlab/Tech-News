from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = []

    query = {"title": {"$regex": title, "$options": "i"}}
    response = search_news(query)

    for new in response:
        news_items = (new["title"], new["url"])
        news.append(news_items)

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
