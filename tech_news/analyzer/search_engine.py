from tech_news.database import search_news
import time


def formatacao_title(news_list):
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 6

def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, "$options": "i"}}
    news_list = search_news(query)
    return formatacao_title(news_list)


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        time.strptime(date, "%Y-%m-%d")
        query = {"timestamp": {"$regex": date}}
        news_date = search_news(query)
        return formatacao_title(news_date)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    query = {"sources": {"$regex": source, "$options": "i"}}
    sources_list = search_news(query)
    return formatacao_title(sources_list)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    query = {"categories": {"$regex": category, "$options": "i"}}
    categories_list = search_news(query)
    return formatacao_title(categories_list)
