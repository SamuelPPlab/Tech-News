from tech_news.database import search_news, find_news, get_collection


# Requisito 6
def search_by_title(title):
    allNews = find_news()
    tuple = []
    for news in allNews:
        if news["title"].lower() == title.lower():
            tuple.append((news["title"], news["url"]))
    return tuple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


search_by_title(
    "Android se beneficia do recurso de rastreamento de apps da Apple"
)

print(search_by_title("x"))
