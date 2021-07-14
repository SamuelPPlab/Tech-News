from tech_news.database import search_news
import datetime


def insensitive(item, attribute):
    query = {f"{attribute}": {"$regex": item, "$options": "i"}}
    return query


def fill_array(list):
    if(len(list) == 0):
        return list
    array = [(item['title'], item['url']) for item in list]
    return array


# Requisito 6
def search_by_title(title):
    query = insensitive(title, "title")
    response_list = search_news(query)
    return fill_array(response_list)


# Requisito 7
# https://stackoverflow.com/questions/4709652/python-regex-to-match-dates
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        response_news_by_date = search_news({"timestamp": {"$regex": date}})
        return fill_array(response_news_by_date)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    query = insensitive(source, "sources")
    response_list = search_news(query)
    return fill_array(response_list)


# Requisito 9
def search_by_category(category):
    query = insensitive(category, "categories")
    response_list = search_news(query)
    return fill_array(response_list)
