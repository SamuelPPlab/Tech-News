from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    result_search = search_news({"title": {"$regex": title, "$options": "i"}})
    if result_search:
        result_one = result_search[0]
        tupla_search = [(result_one["title"], result_one["url"])]
        print(tupla_search)
        return tupla_search
    else:
        return []


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


search_by_title("Vamoscomtudao")
