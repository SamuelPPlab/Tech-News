from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    found_results = search_news(query)
    news_by_title = []

    for news in found_results:
        news_by_title.append((news["title"], news["url"]))

    return news_by_title


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        query = {"timestamp":  {"$regex": date}}
        found_results = search_news(query)
        news_by_date = []

        for news in found_results:
            news_keys = (news["title"], news["url"])
            news_by_date.append(news_keys)
        return news_by_date

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    query = {"sources":  {"$regex": source, "$options": "i"}}
    found_results = search_news(query)
    news_by_source = []

    for news in found_results:
        news_keys = (news["title"], news["url"])
        news_by_source.append(news_keys)
    return news_by_source


# Requisito 9
def search_by_category(category):
    query = {"categories":  {"$regex": category, "$options": "i"}}
    found_results = search_news(query)
    news_by_category = []

    for news in found_results:
        news_keys = (news["title"], news["url"])
        news_by_category.append(news_keys)
    return news_by_category
