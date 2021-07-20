from tech_news.database import search_news
from datetime import datetime


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
def search_by_date(date: str) -> list[tuple]:
    """ - Caso o formato da data seja válido (AAAA-MM-DD):
            - Faz pesquisa por data
            - Retorna uma lista de notícias filtrada pela data
        - Se o formato for incorreto, retorna uma lista vazia.
    """

    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')

    get_news = search_news({"timestamp": {"$regex": date}})

    return [
        (news["title"], news["url"])
        for news in get_news
    ]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
