from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    search_list = search_news(query)
    return [(new["title"], new["url"]) for new in search_list]


# print(search_by_title("espanhol"))


# Requisito 7
def search_by_date(date):
    format = "%Y-%m-%d"
    try:
        datetime.datetime.strptime(date, format)
        query = {"timestamp": {"$regex": date, "$options": "i"}}
        search_list = search_news(query)
        return [(new["title"], new["url"]) for new in search_list]
    except ValueError:
        raise ValueError("Data inválida")


# print(search_by_date("2021-07-10"))


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": source, "$options": "i"}}
    search_list = search_news(query)
    return [(new["title"], new["url"]) for new in search_list]


print(search_by_source("Biel Glasses"))


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": category, "$options": "i"}}
    search_list = search_news(query)
    return [(new["title"], new["url"]) for new in search_list]


print(search_by_category("Minha Série"))
