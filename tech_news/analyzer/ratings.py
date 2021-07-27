from tech_news.database import find_news
import collections
from functools import reduce


# Requisito 10
def top_5_news():
    """
        - Pesquisa no DB e retorna as 5 notícias mais populares;
            - Calcula popularidade pela soma de compartilhamentos e comentários
            - Ordena resultados alfabeticamente por título;
            - Havendo menos de 5 notícias, retorna quantas tiver
    """
    get_all_news = find_news()
    news_info = [
       (
           news["title"], news["url"],
           news["shares_count"] + news["comments_count"]
        )
       for news in get_all_news
    ]
    sorted(news_info, key=lambda news: news[0], reverse=True)
    sorted(news_info, key=lambda news: news[2],)

    news_by_popularity = [
        (info[0], info[1]) for info in news_info
    ]
    return news_by_popularity[:5]


# Requisito 11
def top_5_categories():
    """
        - Pesquisa no DB e retorna as 5 categorias mais recorrentes;
            - Ordena resultados alfabeticamente;
            - Havendo menos de 5 categorias, retorna todas
            - Se não houver categorias, retorna lista vazia
    """
    # Ref. feito com ajuda da Lorena Goes e Rodolfo Martins
    get_all_news = find_news()
    categories = [news["categories"] for news in get_all_news]
    all_categories = reduce(
        lambda categories_list, current: [*categories_list, *current],
        categories, [])
    repeat_counting = list(collections.Counter(all_categories).items())
    repeat_counting.sort(key=lambda category: category[0])
    #  ordena alfebeticamente
    repeat_counting.sort(key=lambda category: category[1], reverse=True)
    #  ordena pela frequência

    pop_categories = [info[0] for info in repeat_counting]
    return pop_categories[:5]
