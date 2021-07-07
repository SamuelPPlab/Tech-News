from tech_news.database import get_collection
import pprint
import datetime


pp = pprint.PrettyPrinter(indent=4)


# Requisito 6
def search_by_title(title):
    title_query = {'title': {'$regex': title, '$options': '-i'}}
    query_filter = {'title': 1, 'url': 1, '_id': 0}
    info = list(get_collection().find(title_query, query_filter))
    # resp_values = list()
    # for item in info:
    #     resp_values.append((item['title'], item['url']))
    # return resp_values
    return [(i['title'], i['url']) for i in info]


# Requisito 7
def search_by_date(date):
    # date_regex = re.compile(
    # r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$')
    # print(date_regex.match(date))
    # if not date_regex.match(date):
    #     raise ValueError('Data inválida')
    date_in_list = date.split('-')
    try:
        wtv = datetime.datetime(
            int(date_in_list[0]), int(date_in_list[1]), int(date_in_list[2]))
        print(wtv)
    except ValueError:
        raise ValueError('Data inválida')
    info = list(get_collection().find(
        {'timestamp': {'$regex': date, '$options': '-i'}},
        {'title': 1, 'url': 1, '_id': 0}
    ))
    return [(i['title'], i['url']) for i in info]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# title = search_by_date('2020-11-23')
# print(type(title))
# print(title)
# title_search = search_by_date('1968-02-30')
# print(type(title_search))
# print(title_search)
