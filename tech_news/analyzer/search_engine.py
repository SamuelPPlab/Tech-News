from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    title_list = search_news({"title": {"$regex": title, "$options": "i"}})
    title_tupla = []
    for tupla in title_list:
        title_tupla.append((tupla["title"], tupla["url"]))

    return title_tupla


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        # referência: https://stackoverflow.com/questions/9978534/
        # match-dates-using-python-regular-expressions/9978804
        date_list = search_news({"timestamp": {"$regex": date}})
    except ValueError:
        raise ValueError("Data inválida")

    date_tupla = []
    for tupla in date_list:
        date_tupla.append((tupla["title"], tupla["url"]))

    return date_tupla


# Requisito 8
def search_by_source(source):
    source_list = search_news({"sources": {"$regex": source, "$options": "i"}})

    source_tupla = []
    for tupla in source_list:
        source_tupla.append((tupla["title"], tupla["url"]))

    return source_tupla


# Requisito 9
def search_by_category(category):
    category_list = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )

    category_tupla = []
    for tupla in category_list:
        category_tupla.append((tupla["title"], tupla["url"]))

    return category_tupla
