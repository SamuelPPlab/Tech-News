from tech_news.database import search_news
import re
import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    busca_noticia = search_news(query)
    lista_tuplas = []
    if busca_noticia is None:
        return lista_tuplas
    else:
        for news in busca_noticia:
            lista_tuplas.append((news["title"], news["url"]))
    return lista_tuplas


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": {"$regex": re.compile(date)}}
    noticia_por_data = search_news(query)
    lista_tuplas = []
    if noticia_por_data is None:
        return lista_tuplas
    else:
        for news in noticia_por_data:
            lista_tuplas.append((news["title"], news["url"]))
    return lista_tuplas


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    query = {"sources": {"$regex": re.compile(source, re.IGNORECASE)}}
    busca_fonte = search_news(query)
    lista_tuplas = []
    if busca_fonte is None:
        return lista_tuplas
    else:
        for news in busca_fonte:
            lista_tuplas.append((news["title"], news["url"]))
    return lista_tuplas


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    query = {"categories": {"$regex": re.compile(category, re.IGNORECASE)}}
    busca_categorias = search_news(query)
    lista_tuplas = []
    if busca_categorias is None:
        return lista_tuplas
    else:
        for news in busca_categorias:
            lista_tuplas.append((news["title"], news["url"]))
    return lista_tuplas
