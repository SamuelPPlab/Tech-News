from tech_news.database import search_news


def filter_columns(new):
    return (new['title'], new['url'])


def validate_date(date):
    year, *_ = date.split('-')
    if len(year) < 4 or int(year) < 2000:
        print(len(year))
        raise ValueError('Data inválida')


# Requisito 6
def search_by_title(title):
    query = {'title': {'$regex': f'.*{title}.*', '$options': "i"}}
    news = search_news(query)

    return [filter_columns(new) for new in news]


# Requisito 7
def search_by_date(date):
    validate_date(date)
    query = {'timestamp': {'$regex': f'.*{date}.*'}}
    news = search_news(query)

    return [filter_columns(new) for new in news]


# Requisito 8
def search_by_source(source):
    query = {'sources': {'$regex': f'.*{source}.*', '$options': "i"}}
    news = search_news(query)

    return [filter_columns(new) for new in news]


# Requisito 9
def search_by_category(category):
    query = {'categories': {'$regex': f'.*{category}.*', '$options': "i"}}
    news = search_news(query)

    return [filter_columns(new) for new in news]
