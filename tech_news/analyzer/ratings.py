from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""


# Requisito 11
def top_5_categories():
    allNews = find_news()
    categories = []
    for aNew in allNews:
        categories = categories + aNew['categories']
    categories.sort()
    return [
        categorie
        for i, categorie in enumerate(categories) if i <= 4
    ]
