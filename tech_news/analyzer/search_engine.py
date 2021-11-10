import datetime
from tech_news.database import get_collection


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    cursor = get_collection().find(
        {"title": {"$regex": title, "$options": "i"}},
        {"_id": False, "title": True, "url": True},
    )
    result = []
    for item in cursor:
        result.append((item["title"], item["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    format = "%Y-%m-%d"
    try:
        datetime.datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Data inválida")

    cursor = get_collection().find({"timestamp": {"$regex": date}})
    result = []
    for item in cursor:
        result.append((item["title"], item["url"]))
    return result


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    cursor = get_collection().find(
        {"sources": {"$regex": source, "$options": "i"}}
    )
    result = []
    for item in cursor:
        result.append((item["title"], item["url"]))
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    cursor = get_collection().find(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    result = []
    for item in cursor:
        result.append((item["title"], item["url"]))
    return result
