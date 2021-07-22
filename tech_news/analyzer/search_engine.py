from tech_news.database import search_news
import datetime as dt


# https://www.geeksforgeeks.org/string-capitalize-python/
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
# https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python
# Ajuda Emerson e Anderson
def search_by_date(date):
    format = '%Y-%m-%d'
    result = []
    try:
        dt.datetime.strptime(date, format)
        response = search_news({'timestamp': {'$regex': date}})
        if len(response) == 0:
            return result

        dict_response = response[0]
        response_title = dict_response['title']
        response_url = dict_response['url']
        tuple_response = (response_title, response_url)
        result.append(tuple_response)

        return result
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_source(source):
    result = []
    response = search_news({"sources": {'$regex': source, '$options': '-i'}})

    print(response)
    if len(response) == 0:
        print(response)
        return result

    for news in response:
        response_title = news['title']
        response_url = news['url']
        tuple_response = (response_title, response_url)
        result.append(tuple_response)

    return result


# Requisito 9
def search_by_category(category):
    result = []
    response = search_news(
        {"categories": {'$regex': category, '$options': '-i'}}
    )

    print(response)
    if len(response) == 0:
        print(response)
        return result

    for news in response:
        response_title = news['title']
        response_url = news['url']
        tuple_response = (response_title, response_url)
        result.append(tuple_response)

    return result
