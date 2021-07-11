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
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
