from tech_news.database import find_news


def order_news_popularity(new):
    return new['shares_count'] + new['comments_count']


def column_filtered(index, new):
    return (f'noticia_{index + 1}',  new['url'])


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news = find_news()
    news.sort(key=order_news_popularity, reverse=True)
    return [
        column_filtered(index, new)
        for index, new in enumerate(news) if index <= 4
    ]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
