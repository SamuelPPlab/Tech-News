from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    noticias = search_news({
        "title": {"$regex": f"{title}", "$options": "i"}
    })
    noticias_formatadas = []
    for noticia in noticias:
        noticias_formatadas.append((noticia["title"], noticia["url"]))
    return noticias_formatadas


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
