from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """ - Recebe uma string, faz pesquisa case-insentive por títulos de notícias e:
        - Retorna a notícia caso haja correspondência e uma lista vazia se não.
    """
    # Ref: Bruna Sepulveda + encurtador.com.br/bpLQ2

    get_news = search_news({"title": {"$regex": title, "$options": "i"}})

    return [
        (news["title"], news["url"])
        for news in get_news
    ]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


teste = 'CAIXA_ALTA'
print(teste.lower())
