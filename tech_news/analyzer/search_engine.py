from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    title = title.lower().capitalize()
    response = search_news({"title": title})
    if response:
        tupla_response = [(response[0].get("title"), response[0].get("url"))]
    else:
        tupla_response = []
    return tupla_response


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
