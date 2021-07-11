from tech_news.database import find_news


# Requisito 6
def search_by_title(title):
    title = title.lower()
    noticias = find_news()
    noticias_com_title = [
        (noticia["title"], noticia["url"])
        for noticia in noticias if title in noticia["title"].lower()
    ]
    return noticias_com_title


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
