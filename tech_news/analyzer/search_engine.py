from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    result = search_news({'title': {'$regex': title, '$options': 'i'}})
    # Referência: projetod a Thays Costa
    list_of_news = []

    for new in result:
        list_of_news.append((new['title'], new['url']))

    return list_of_news


# Requisito 7
def search_by_date(date):
    regex = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    # Ref: https://stackoverflow.com/questions/1711727/
    # regular-expression-to-match-dates-in-yyyy-mm-dd-format
    try:
        regex.match(date)

    except ValueError:
        raise ValueError("Data inválida")

    result = search_news({'timestamp': {'$regex': date}})
    list_of_news = []

    for new in result:
        list_of_news.append((new['title'], new['url']))
    return list_of_news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""