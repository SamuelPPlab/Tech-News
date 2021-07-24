from tech_news.database import search_news
import re
import datetime

# Requisito 6


def search_by_title(title):
    # print(title) Vamoscomtudo
    pattern = re.compile(f'.*{title}.*', re.IGNORECASE)
    # print(pattern) VAMOSCOMTUDO
    results = search_news({"title": pattern})
    news = []
    for result in results:
        search = (result["title"], result["url"])
        news.append(search)
    return news

# Requisito 7


def search_by_date(date):
    # https://www.alura.com.br/artigos/lidando-com-datas-e-ho
    # rarios-no-python?gclid=Cj0KCQjw0emHBhC1ARIsAL1QGNenAki-Y
    # -E31W-lEdbyx9IO3fNaFElYiqlNFVBAGEc5h52Wvxzunx0aAhlVEALw_wcB
    # print(type(date)) <class 'str'>
    datetime

    

search_by_date("2020-11-23T11:00:01")

# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
