from tech_news.database import search_news, get_collection
from datetime import datetime


# Requisito 6
def search_by_title(title):
    title = title.lower().capitalize()
    response = search_news({"title": title})
    tupla_response = response_treatment(response)
    return tupla_response


def response_treatment(response):
    if response:
        tupla_response = [(response[0].get("title"), response[0].get("url"))]
    else:
        tupla_response = []
    return tupla_response


# Requisito 7
def search_by_date(date):
    try:
        # year, month, day = date.split("-")
        # datetime(int(year), int(month), int(day))
        datetime.strptime(date, "%Y-%m-%d")
        initial_date_time = date + "T00:00:00.000Z"
        finally_date_time = date + "T24:59:59.000Z"
        response = list(
            get_collection().find(
                {
                    "timestamp": {
                        "$gte": (initial_date_time),
                        "$lte": (finally_date_time),
                    }
                }
            )
        )
        tupla_response = response_treatment(response)
        return tupla_response
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    response = list(
        get_collection().find({"sources": {"$regex": source, "$options": "i"}})
    )
    tupla_response = response_treatment(response)
    return tupla_response


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
