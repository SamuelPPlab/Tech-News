from tech_news.database import search_news
import re


def filterTitlesAndUrl(news):
    newList = []
    for new in news:
        newList.append((new["title"], new["url"]))
    return newList


# Requisito 6
def search_by_title(title):
    news = search_news(
        {"title": {"$regex": title, "$options": "-i"}}
    )
    newList = filterTitlesAndUrl(news)
    return newList


# Requisito 7
def search_by_date(date):
    regex = r"^(20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$"
    if (re.search(regex, date)):
        query = {"timestamp": {"$regex": f"(?i){date}"}}
        noticias = search_news(query)
        result = []
        for noticia in noticias:
            tempArray = []
            tempArray.append(noticia["title"])
            tempArray.append(noticia["url"])
            result.append(tuple(tempArray))
        return result
    else:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


search_by_date("2020-11-23")
