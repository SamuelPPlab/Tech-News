from tech_news.database import find_news
from functools import reduce
import collections


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    all_news = find_news()
    infos_news = [
        (
            news["title"], news["url"],
            news["shares_count"] + news["comments_count"]
        )
        for news in all_news
    ]
    sorted(infos_news, key=lambda news: news[0], reverse=True)
    sorted(infos_news, key=lambda news: news[2],)

    popularity_list_news = [
        (info[0], info[1]) for info in infos_news
    ]
    return popularity_list_news[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    all_news = find_news()
    categories = [news["categories"] for news in all_news]
    all_categories = reduce(
        lambda categories_list, current: [*categories_list, *current],
        categories, [])
    couting = list(collections.Counter(all_categories).items())
    couting.sort(key=lambda category: category[0])
    #  ordena alfebeticamente
    couting.sort(key=lambda category: category[1], reverse=True)
    #  ordena pela frequência

    categories_pop = [info[0] for info in couting]
    return categories_pop[:5]
