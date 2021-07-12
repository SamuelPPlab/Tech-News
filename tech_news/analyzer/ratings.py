from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    top = []
    for new in news:
        new['popularity'] = new['shares_count'] + new['comments_count']
    news = sorted(news, key=lambda x: x['title'])
    news = sorted(news, key=lambda x: x['popularity'], reverse=True)

    for new in news[:5]:
        top.append((new['title'], new['url']))

    return top


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
