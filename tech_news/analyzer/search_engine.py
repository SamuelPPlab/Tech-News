from tech_news.database import search_news
import re
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Busca por titulo do Banco de dados"""
    search = {"title": {"$regex": title, "$options": "i"}}
    result = search_news(search)
    return [(news["title"], news["url"]) for news in result]


# Requisito 7
def search_by_date(date):
    """Faz busca por data"""
    try:
        date = datetime.strptime(date, "%d/%m/%Y")
    except Exception:
        raise ValueError("Data inválida")

    search = {"timestamp": {"$regex": date}}
    result = search_news(search)
    return [(news["title"], news["url"]) for news in result]


# Requisito 8
def search_by_source(source):
    """Realiza busca por fonte"""
    try:
        source = source.lower()
    except AttributeError:
        raise ValueError("Fonte inválida")

    rgx = re.compile(source, re.IGNORECASE)
    search = {"sources": {"$regex": rgx}}
    result = search_news(search)
    return [(news["title"], news["url"]) for news in result]


# Requisito 9
def search_by_category(category):
    """Procura no banco por categoria"""
    try:
        searchCat = category.lower()
    except AttributeError:
        raise ValueError("Categoria inválida")

    rgx = re.compile(searchCat, re.IGNORECASE)
    search = {"categories": {"$regex": rgx}}
    result = search_news(search)
    return [(news["title"], news["url"]) for news in result]
