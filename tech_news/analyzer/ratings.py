from tech_news.database import find_news


# Requisito 10
def top_5_news():
    search = find_news()
    for res in search:
        res['popularity'] = res['shares_count'] + res['comments_count']
    sorted_news = sorted(search, key=lambda x: x['title'])
    sorted_news = sorted(
        sorted_news, key=lambda x: x['popularity'], reverse=True
    )
    top_5 = []
    for news in sorted_news[:5]:
        top_5.append((news['title'], news['url']))
    return top_5


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
