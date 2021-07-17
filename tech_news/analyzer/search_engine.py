from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Procura a noticia pelo titulo e retorna uma tupla com titulo e url"""
    noticias = search_news({"title": {"$regex": title, "$options": "i"}})
    titulo_url = []
    for noticia in noticias:
        titulo_url.insert(len(titulo_url), (noticia["title"], noticia["url"]))
    return titulo_url


# Requisito 7
def search_by_date(date):
    """Procura a noticia pela data e retorna uma tupla com titulo e url"""
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    noticias = search_news({"timestamp": {"$regex": f".*{date}.*"}})
    titulo_url = []
    for noticia in noticias:
        titulo_url.insert(len(titulo_url), (noticia["title"], noticia["url"]))
    return titulo_url


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
