from tech_news.database import find_news


def popularity(new):
    popularity_news = (new['shares_count'] + new['comments_count'])
    return popularity_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news = find_news()
    # Referencia Vitor Rodrigues
    sort_new = sorted(news, key=popularity, reverse=True)
    top_5_new = [(new["title"], new["url"]) for new in sort_new[:5]]
    return top_5_new


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
