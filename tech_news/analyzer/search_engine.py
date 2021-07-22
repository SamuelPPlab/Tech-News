from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    result = []
    param = title.lower()
    param = param.capitalize()
    response = search_news({"title": param})

    if len(response) == 0:
        return result

    dict_response = response[0]
    response_title = dict_response['title']
    response_url = dict_response['url']
    tuple_response = (response_title, response_url)
    result.append(tuple_response)
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
