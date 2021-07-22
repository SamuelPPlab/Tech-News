from tech_news.database import find_news
from operator import itemgetter
from collections import Counter


# Requisito 10
def top_5_news():
    """Retorna as 5 mais populares"""
    allNews = find_news()

    listPopular = sorted(
        allNews,
        key=lambda news: news["shares_count"] + news["comments_count"],
        reverse=True,
    )

    listByName = sorted(listPopular, key=itemgetter("title"))

    titleUri = []

    for noticia in listByName:
        titleUri.insert(len(titleUri), (noticia["title"], noticia["url"]))
    return titleUri[:5]


# Requisito 11
def top_5_categories():
    """5 noticias mais populares por categoria"""

    news = find_news()
    listCategories = []
    categorieValue = []

    for n in news:
        for c in n["categories"]:
            listCategories.append(c)

    countCategories = Counter(listCategories).most_common()
    result = sorted(countCategories)

    for r in result:
        categorieValue.append(r[0])

    return categorieValue[:5]
