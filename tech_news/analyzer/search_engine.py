# Requisito 6
from tech_news.database import search_news


def filter_by_column(new):
    return (new['title'], new['url'])


def search_by_title(title):
    query = {'title': {'$regex': f'.*{title}.*', '$options': "i"}}
    news = search_news(query)

    return [filter_by_column(new) for new in news]


# Requisito 7
def search_by_date(date):
    year, *_ = date.split('-')
    if len(year) < 4 or int(year) < 2000:
        print(len(year))
        raise ValueError('Data inválida')
    query = {'timestamp': {'$regex': f'.*{date}.*'}}
    news = search_news(query)

    return [filter_by_column(new) for new in news]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
