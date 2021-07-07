from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


# Requisito 6
def search_by_title(title):
    lista_tupla = []
    lista = list(
        db.news.find(
            {"title": {"$regex": title, "$options": "-i"}},
            {"_id": 0, "title": 1, "url": 1},
        )
    )
    for i in lista:
        lista_tupla.append((i["title"], i["url"]))
    return lista_tupla


# Requisito 7
def search_by_date(date):
    
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
