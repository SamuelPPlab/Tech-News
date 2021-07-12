from tech_news.database import get_collection
import re


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": '(?i)'+title}}
    noticia = get_collection()
    result = noticia.find(query, {"_id": 0, "title": 1, "url": 1})
    resposta = []
    for i in result:
        empty = []
        empty.append(i["title"])
        empty.append(i["url"])
        resposta.append(tuple(empty))
    return resposta


# Requisito 7
def search_by_date(date):
    regex = r"^(20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$"
    match = re.search(regex, date)
    if match:
        query = {"timestamp": {"$regex": f"(?i){date}"}}
        noticia = get_collection()
        result = noticia.find(query, {"_id": 0, "title": 1, "url": 1})
        resposta = []
        for i in result:
            empty = []
            empty.append(i["title"])
            empty.append(i["url"])
            resposta.append(tuple(empty))
        return resposta
    else:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$regex": '(?i)'+source}}
    noticia = get_collection()
    result = noticia.find(query, {"_id": 0, "title": 1, "url": 1})
    resposta = []
    for i in result:
        empty = []
        empty.append(i["title"])
        empty.append(i["url"])
        resposta.append(tuple(empty))
    return resposta


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": '(?i)'+category}}
    noticia = get_collection()
    result = noticia.find(query, {"_id": 0, "title": 1, "url": 1})
    resposta = []
    for i in result:
        empty = []
        empty.append(i["title"])
        empty.append(i["url"])
        resposta.append(tuple(empty))
    return resposta
