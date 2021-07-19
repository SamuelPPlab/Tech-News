from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    result_search = search_news({"title": {"$regex": title, "$options": "i"}})
    if result_search:
        result_one = result_search[0]
        tupla_search = [(result_one["title"], result_one["url"])]
        return tupla_search
    else:
        return []


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        result_search = search_news({"timestamp": {"$regex": date}})
        if result_search:
            result_one = result_search[0]
            tupla_search = [(result_one["title"], result_one["url"])]
            return tupla_search
        else:
            return []
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    result_search = search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    if result_search:
        result_one = result_search[0]
        tupla_search = [(result_one["title"], result_one["url"])]
        return tupla_search
    else:
        return []


# Requisito 9
def search_by_category(category):
    result_search = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    if result_search:
        result_one = result_search[0]
        tupla_search = [(result_one["title"], result_one["url"])]
        return tupla_search
    else:
        return []


search_by_source("Venture Beat")
