from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    titles_results = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(title["title"], title["url"]) for title in titles_results]


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        date_results = search_news({"timestamp": {"$regex": date}})
        return [(results["title"], results["url"]) for results in date_results]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    source_results = search_news(
        {"sources": {"$regex": source, "$options": "i"}})
    return [(results["title"], results["url"]) for results in source_results]


# Requisito 9
def search_by_category(category):
    category_results = search_news(
        {"categories": {"$regex": category, "$options": "i"}})
    return [(results["title"], results["url"]) for results in category_results]
