from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    title_list = list(
        db.news.find(
            {"title": {"$regex": title, "$options": "-i"}},
            {"_id": 0, "title": 1, "url": 1},
        )
    )
    title_list_tupla = []
    for item in title_list:
        title_list_tupla.append((item["title"], item["url"]))
    return title_list_tupla


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
