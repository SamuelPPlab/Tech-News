from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    info = list()
    news = search_news({"title": {"$regex": title, "$options": "si"}})
    for news_item in news:
        if news_item["title"]:
            get_tuple = (news_item["title"], news_item["url"])
            info.append(get_tuple)
    return info


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
