from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def format_title_url(news_list):
    return [(news["title"], news["url"]) for news in news_list]


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news_list = search_news(query)
    return format_title_url(news_list)


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        query = {"timestamp": {"$regex": date}}
        news_date = search_news(query)
        return format_title_url(news_date)
    except ValueError:
        raise ValueError("Data Inválida")


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": source, "$options": "i"}}
    sources_list = search_news(query)
    return format_title_url(sources_list)


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": category, "$options": "i"}}
    categories_list = search_news(query)
    return format_title_url(categories_list)
