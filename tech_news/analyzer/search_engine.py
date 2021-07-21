from tech_news.database import db
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_title_url = []
    for news in db.news.find({"title": {"$regex": title, "$options": "i"}}):
        news_title_url.append((news["title"], news["url"]))
    return(news_title_url)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    format = "%Y-%m-%d"
    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news_title_url = []
        for news in db.news.find(
            {"timestamp": {"$regex": date, "$options": "i"}}
        ):
            news_title_url.append((news["title"], news["url"]))
        return news_title_url


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    news_title_url = []
    for news in db.news.find({"sources": {"$regex": source, "$options": "i"}}):
        news_title_url.append((news["title"], news["url"]))
    return news_title_url


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news_title_url = []
    for news in db.news.find(
        {"categories": {"$regex": category, "$options": "i"}}
    ):
        news_title_url.append((news["title"], news["url"]))
    return news_title_url
