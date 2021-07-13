from tech_news.database import get_collection
from operator import itemgetter


def top_5_news():
    news_popularity = []
    all_news = get_collection().find()
    for news in all_news:
        popularity = news["shares_count"] + news["comments_count"]
        tupla = (news['title'], news['url'], popularity)
        news_popularity.append(tupla)
    news_popularity = sorted(
        news_popularity, key=itemgetter(2), reverse=True
    )
    popular = []
    if len(news_popularity) >= 5:
        for n in range(0, 5):
            pop = news_popularity[n]
            tupla = (pop[0], pop[1])
            popular.append(tupla)
    else:
        for n in range(0, len(news_popularity)):
            pop = news_popularity[n]
            tupla = (pop[0], pop[1])
            popular.append(tupla)

    return popular


def fun(x, list):
    for item in list:
        print(x)


# Requisito 11
def categories(list_news):
    all_categories = set()
    for news in list_news:
        for category in news["categories"]:
            all_categories.add(category)
    return all_categories


def top_5_categories():
    """Seu código deve vir aqui"""
