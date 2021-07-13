import datetime
from tech_news.database import find_news, search_news


# Requisito 6
def search_by_title(title):
    all_news = find_news()
    result = []

    for news in all_news:
        if title.lower() in news['title'].lower():
            result.append((news['title'], news['url']))
    return result


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        find_date = search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")
    mylist = []
    for index in find_date:
        mylist.append((index['title'], index['url']))
    return mylist


# Requisito 8
def search_by_source(source):
    try:
        find_source = search_news({
            "sources": {"$regex": source, "$options": "i"}})
    except ValueError:
        raise ValueError("Data inválida")
    mylist = []
    for index in find_source:
        mylist.append((index['title'], index['url']))
    return mylist


# Requisito 9
def search_by_category(category):
    try:
        find_category = search_news({
            "categories": {"$regex": category, "$options": "i"}})
    except ValueError:
        raise ValueError("Data inválida")
    mylist = []
    for index in find_category:
        mylist.append((index['title'], index['url']))
    return mylist
