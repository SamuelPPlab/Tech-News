from pymongo import MongoClient
from decouple import config
import re

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news

# Requisito 6


def search_by_title(title):
    lista = []
    xablau = list(
        db.news.find(
            {"title": {"$regex": title, "$options": "-i"}},
            {"_id": 0, "title": 1, "url": 1},
        )
    )

    for i in xablau:
        lista.append((i["title"], i["url"]))

    return lista


# Requisito 7
def search_by_date(date):

    date_regex = r"^20\d{2}-(0[1-9]|1[0-2])-(0[1-9]|1\d|2\d|3[01])$"
    if re.search(date_regex, date) is None:
        raise ValueError("Data inválida")

    xablau = list(
        db.news.find(
            {"timestamp": {"$regex": date, "$options": "-i"}},
            {"_id": 0, "title": 1, "url": 1},
        )
    )

    lista = []

    for i in xablau:
        lista.append((i["title"], i["url"]))

    return lista


# Requisito 8
def search_by_source(source):
    lista = []
    xablau = list(
        db.news.find(
            {"sources": {"$regex": source, "$options": "-i"}}
        )
    )

    for i in xablau:
        lista.append((i["title"], i["url"]))

    return lista


# Requisito 9
def search_by_category(category):
    lista = []
    xablau = list(
        db.news.find(
            {"categories": {"$regex": category, "$options": "-i"}}
        )
    )

    for i in xablau:
        lista.append((i["title"], i["url"]))

    return lista
