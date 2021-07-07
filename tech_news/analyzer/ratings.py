from tech_news.database import find_news

def order_news_popularity(new):
    return new['shares_count'] + new['comments_count']

def filter_columns(ind, new):
    return (f'noticia_{ind + 1}',  new['url'])

# Requisito 10
def top_5_news():
    news = find_news()
    news.sort(key=order_news_popularity, reverse=True)
    return [
        filter_columns(index, new)
        for index, new in enumerate(news) if index <= 4
    ]


# Requisito 11
def top_5_categories():
    news = find_news()
    list_categories = []
    for new in news:
        list_categories = list_categories + new['categories']
    list_categories.sort()
    return [
        categorie
        for index, categorie in enumerate(list_categories) if index <= 4
    ]
