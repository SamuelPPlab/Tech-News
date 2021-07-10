from tech_news.database import search_news
from datetime import datetime


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
    date_format = "%Y-%m-%d"
    try:
        datetime.strptime(date, date_format)
    except ValueError:
        raise ValueError("Data inválida")
    else:
        noticias = search_news({
            "timestamp": {"$regex": f"{date}", "$options": "i"}
        })
        noticias_formatadas = []
        for noticia in noticias:
            noticias_formatadas.append((noticia["title"], noticia["url"]))
        return noticias_formatadas


# Requisito 8
def search_by_source(source):
    noticias = search_news({
        "sources": {"$regex": f"{source}", "$options": "i"}
    })
    noticias_formatadas = []
    for noticia in noticias:
        noticias_formatadas.append((noticia["title"], noticia["url"]))
    return noticias_formatadas


# Requisito 9
def search_by_category(category):
    noticias = search_news({
        "categories": {"$regex": f"{category}", "$options": "i"}
    })
    noticias_formatadas = []
    for noticia in noticias:
        noticias_formatadas.append((noticia["title"], noticia["url"]))
    return noticias_formatadas
