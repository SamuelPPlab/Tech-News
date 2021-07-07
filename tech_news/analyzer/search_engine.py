import tech_news.database
import datetime


def validate(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 6
def search_by_title(title):
    search = tech_news.database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    results = [
        (result["title"], result["url"]) for result in search
    ]
    return results


# Requisito 7
def search_by_date(date):
    validate(date)
    search = tech_news.database.search_news(
        {"timestamp": {"$regex": date}}
    )

    results = [
        (result["title"], result["url"]) for result in search
    ]
    return results


# Requisito 8
def search_by_source(source):
    search = tech_news.database.search_news(
        {"sources": {"$regex": source, "$options": "i"}}
    )

    results = [
        (result["title"], result["url"]) for result in search
    ]
    return results


# Requisito 9
def search_by_category(category):
    search = tech_news.database.search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )

    results = [
        (result["title"], result["url"]) for result in search
    ]
    return results
