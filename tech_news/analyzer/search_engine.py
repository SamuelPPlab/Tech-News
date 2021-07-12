from tech_news.database import get_collection


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


