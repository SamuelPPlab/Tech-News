from tech_news.database import search_news
import re


def extract_data(data):
    return(data['title'], data['url'])


# Requisito 6
def search_by_title(title):
    response = search_news({'title': {'$regex': title, '$options': 'i'}})
    result = []
    for data in response:
        result.append(extract_data(data))
    return result


# Requisito 7
def search_by_date(date):
    regex_date = r'^20\d{2}-(0[1-9]|1[0-2])-(0[1-9]|1\d|2\d|3[01])$'
    if (re.search(regex_date, date) is None):
        raise ValueError("Data inválida")
    response = search_news({'timestamp': {'$regex': date}})
    result = []
    for data in response:
        result.append(extract_data(data))
    return result


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# result = search_by_title("Vamoscomtudo")
# print(result)
