from tech_news.database import search_news
from datetime import datetime


# Requisito 6
# Video sobre regex: egexhttps://www.youtube.com/watch?v=O7VFp5fzZuE
def search_by_title(title):
    # '$regex': title, procura aonde tem a palavra title
    # '$options': 'i' não diferencia maiúsculas de minúsculas
    items = search_news({"title": {"$regex": title, "$options": "i"}})
    new_list = [(item["title"], item["url"]) for item in items]
    return new_list


# Requisito 7
def search_by_date(date):
    # https://qastack.com.br/programming/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
    # https://www.journaldev.com/33500/python-valueerror-exception-handling-examples
    # https://www.programiz.com/python-programming/datetime/strptime
    format_date = "%Y-%m-%d"
    try:
        datetime.today().strptime(date, format_date)

        data = search_news({"timestamp": {"$regex": date}})
        new_list = [(item["title"], item["url"]) for item in data]
        return new_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    items = search_news({"sources": {"$regex": source, "$options": "i"}})
    new_list = [(item["title"], item["url"]) for item in items]
    return new_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    items = search_news({"categories": {"$regex": category, "$options": "i"}})
    new_list = [(item["title"], item["url"]) for item in items]
    return new_list
