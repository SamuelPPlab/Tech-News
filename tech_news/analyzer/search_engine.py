import datetime

from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    find_title = search_news({"title": {"$regex": title, "$options": "i"}})
    mylist = []
    for index in find_title:
        mylist.append((index['title'], index['url']))
    return mylist


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
