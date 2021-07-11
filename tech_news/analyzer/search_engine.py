from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    title = title.lower()
    noticias = find_news()
    return [
        (noticia["title"], noticia["url"])
        for noticia in noticias if title in noticia["title"].lower()
    ]


# Requisito 7
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")


def search_by_date(date):
    validate_date(date)
    noticias = find_news()
    return [
        (noticia["title"], noticia["url"])
        for noticia in noticias if date == noticia["timestamp"][:10]
    ]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
