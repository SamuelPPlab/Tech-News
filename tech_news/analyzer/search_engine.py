from tech_news.database import search_news


# Requisito 6
# Video sobre regex: egexhttps://www.youtube.com/watch?v=O7VFp5fzZuE
def search_by_title(title):
    # '$regex': title, procura aonde tem a palavra title
    # '$options': 'i' não diferencia maiúsculas de minúsculas
    items = search_news({"title": {"$regex": title, "$options": "i"}})
    # print(items)
    # new_list = []
    # for item in items:
    #     lista = [(item["title"], item["url"])]
    #     new_list.append(lista)
    new_list = [(item["title"], item["url"]) for item in items]
    return new_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
