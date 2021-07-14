from tech_news.database import search_news
import datetime


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
    # https://www.programiz.com/python-programming/datetime/strptime
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        get_news_by_date = search_news(
            {"timestamp": {"$regex": date}}
        )
        title_and_url = []
        for news in get_news_by_date:
            title_and_url.insert(
                len(title_and_url), (news["title"], news["url"])
            )
        return title_and_url
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    # Bloco 24 - MongoDB: Updates Simples e Complexos - regex
    get_news = search_news({"sources": {"$regex": source, "$options": "i"}})
    title_and_url = []
    for news in get_news:
        title_and_url.insert(len(title_and_url), (news["title"], news["url"]))
    return title_and_url



# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
