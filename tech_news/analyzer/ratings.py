from tech_news.database import find_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    """retorna as 5 notícias mais populares"""
    todas_noticias = find_news()

    lista_por_popularidade = sorted(
        todas_noticias,
        key=lambda news: news["shares_count"] + news["comments_count"],
        reverse=True,
    )

    lista_por_nomes = sorted(lista_por_popularidade, key=itemgetter("title"))

    titulo_url = []

    for noticia in lista_por_nomes:
        titulo_url.insert(len(titulo_url), (noticia["title"], noticia["url"]))
    return titulo_url[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
