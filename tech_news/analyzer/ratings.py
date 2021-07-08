# Requisito 10
from tech_news.database import find_news


def top_5_news():
    lista_ordenada = sorted(
        [
            (item["shares_count"] + item["comments_count"])
            for item in find_news()
        ]
    )
    return [
        (f'noticia_{index + 1}',  item['url']) 
        for index, item in enumerate(lista_ordenada) if index <= 4
    ]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""


top_5_news()
