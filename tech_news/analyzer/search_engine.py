from pymongo import MongoClient
from decouple import config
from datetime import datetime


DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


# Requisito 6
def search_by_title(title):
    # """Seu código deve vir aqui"""
    title_list = list(
        db.news.find({"title": {"$regex": title, "$options": "-i"}})
    )
    # title_list_tupla = []
    # for item in title_list:
    #     title_list_tupla.append((item["title"], item["url"]))
    # return title_list_tupla
    return [(item["title"], item["url"]) for item in title_list]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
        date_list = list(db.news.find({"timestamp": {"$regex": date}}))
        return [(item["title"], item["url"]) for item in date_list]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    source_list = list(
        db.news.find({"sources": {"$regex": source, "$options": "-i"}})
    )
    return [(item["title"], item["url"]) for item in source_list]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    category_list = list(
        db.news.find({"categories": {"$regex": category, "$options": "-i"}})
    )
    return [(item["title"], item["url"]) for item in category_list]

# search_by_title('Vamo')
# search_by_date("2020-11-23")
# search_by_source(["ResetEra"])
