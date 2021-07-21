from tech_news.database import search_news
import re
import datetime


# Requisito 6
def search_by_title(title):
    result = search_news({'title': {'$regex': title, '$options': 'i'}})
    # Referência: projetod a Thays Costa
    list_of_news = []

    for new in result:
        list_of_news.append((new['title'], new['url']))

    return list_of_news


def test_valid_date(date):
    # Ref: https://www.codevscolor.com/date-valid-check-python#:~:
    # text=Python%20Program%20%3A&text=split('%2F')%20isValidDate,
    # is%20not%20valid..%22)&text=If%20its%20value%20is%20'True,
    # date%2C%20else%20it%20is%20not.
    year, month, day = date.split('-')

    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_date(date):
    regex = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    # Ref: https://stackoverflow.com/questions/1711727/
    # regular-expression-to-match-dates-in-yyyy-mm-dd-format

    test_valid_date(date)

    try:
        valid_format = bool(regex.match(date))
        if valid_format:
            result = search_news({'timestamp': {'$regex': date}})
            list_of_news = []

            for new in result:
                list_of_news.append((new['title'], new['url']))
            return list_of_news

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    result = search_news({'sources': {'$regex': source, '$options': 'i'}})
    # Referência: projetod a Thays Costa
    list_of_news = []

    for new in result:
        list_of_news.append((new['title'], new['url']))

    return list_of_news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
