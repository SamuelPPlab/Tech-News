from tech_news.database import get_collection


def popularity(x):
    return x["shares_count"] + x["comments_count"]


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    collection = sorted(
        list(get_collection().find({}, {"title": 1, "url": 1, "_id": 0})),
        key=lambda elem: (popularity, "name"),
        reverse=True,
    )
    if len(collection) > 5:
        collection = collection[:5]
    return [((item["title"], item["url"])) for item in collection]


def filtro(x):
    return x[0]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    collection = list(get_collection().find({}, {"categories": 1, "_id": 0}))
    dic = {}
    for item in collection:
        for sub_item in item["categories"]:
            if sub_item in dic.keys():
                dic[sub_item] += +1
            else:
                dic[sub_item] = 1
    lista = sorted(dic.items(), key=lambda k: k[0])
    lista = sorted(lista, key=lambda k: k[1])
    lista = list(map(filtro, lista))
    if len(lista) > 5:
        lista = lista[:5]
    return lista
