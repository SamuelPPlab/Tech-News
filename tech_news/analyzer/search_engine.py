from tech_news.database import get_collection
import re


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    found = get_collection().find(
        {"title": {"$regex": title, "$options": "-i"}}
    )
    found = list(found)
    result = []
    for item in found:
        result.append((item["title"], item["url"]))
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    test = re.search(
        "^20[0-2][0-9]-((0[1-9])|(1[0-2]))-([0-2][1-9]|3[0-1])$", date)
    if not test:
        raise ValueError('Data inválida')
    else:
        # found = list(get_collection().find({"timestamp": date}))
        found = get_collection().find(
            {"timestamp": {"$regex": date}})
        return [((item["title"], item["url"]))for item in found]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    found = list(get_collection().find({
        "sources": {'$elemMatch': {'$regex': source, '$options': 'i'}}}))
    print('found', found)
    return [((item["title"], item["url"]))for item in found]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    found = list(get_collection().find({
        "categories": {'$elemMatch': {'$regex': category, '$options': 'i'}}}))
    print('found', found)
    return [((item["title"], item["url"]))for item in found]
