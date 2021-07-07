from tech_news.database import get_collection
import pprint


pp = pprint.PrettyPrinter(indent=4)


# Requisito 6
def search_by_title(title):
    title_query = {'title': {'$regex': title, '$options': '-i'}}
    query_filter = {'title': 1, 'url': 1, '_id': 0}
    info = list(get_collection().find(title_query, query_filter))
    resp_values = list()
    for item in info:
        resp_values.append((item['title'], item['url']))
    return resp_values


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# title_search = search_by_title('é')
# print(type(title_search))
