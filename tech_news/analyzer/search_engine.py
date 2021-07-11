from tech_news.database import search_news
# https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python?gclid=EAIaIQobChMIk8i_z7jb8QIVkgyRCh3JhABGEAAYASAAEgJ8xPD_BwE
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = []

    query = {"title": {"$regex": title, "$options": "i"}}
    response = search_news(query)

    for new in response:
        news_items = (new["title"], new["url"])
        news.append(news_items)

    return news


# Requisito 7
def search_by_date(date):
    date_format = "%Y-%m-%d"
    news = []

# https://docs.python.org/3/tutorial/errors.html
    try:
        datetime.strptime(date, date_format)
    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": {"$regex": date}}
    response = search_news(query)

    for new in response:
        news_items = (new["title"], new["url"])
        news.append(news_items)

    return news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
