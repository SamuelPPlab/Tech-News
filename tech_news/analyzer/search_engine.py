from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    title_and_url_news = []
    all_news = search_news(
        {"title": {"$regex": f"{title}", "$options": "i"}}
    )  # query @rafaelmguimaraes

    for news in all_news:
        title_and_url_news.append((news["title"], news["url"]))
    return title_and_url_news


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        title_and_url_news = []
        all_news = search_news(
            {"timestamp": {"$regex": f"{date}", "$options": "i"}}
        )
        for news in all_news:
            title_and_url_news.append((news["title"], news["url"]))
        return title_and_url_news

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
