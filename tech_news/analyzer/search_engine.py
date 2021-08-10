from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "si"}})
    searchResults = list()

    for item in news:
        searchResults.append((item["title"], item["url"]))

    return searchResults


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news = search_news({"timestamp": {"$regex": date}})
        searchResults = list()

        for item in news:
            searchResults.append((item["title"], item["url"]))

        return searchResults


def search_by_source(source):
    news = search_news({"sources": {"$regex": source, "$options": "si"}})
    searchResults = list()

    for item in news:
        searchResults.append((item["title"], item["url"]))

    return searchResults


def search_by_category(category):
    news = search_news({"categories": {"$regex": category, "$options": "si"}})
    searchResults = list()

    for item in news:
        searchResults.append((item["title"], item["url"]))

    return searchResults
