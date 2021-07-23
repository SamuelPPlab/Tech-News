from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_found = find_news()

    news_popularity = [
        (news['shares_count'] + news['comments_count'],
            news['title'], news['url'])
        for news in news_found
    ]

    news_popularity_sorted = sorted(news_popularity, key=lambda var: var[1])
    news_popularity_sorted = sorted(
        news_popularity, key=lambda var: var[0], reverse=True)

    top_five_categories = []

    for news in news_popularity_sorted:
        news_keys = (news[1], news[2])
        top_five_categories.append(news_keys)

    return top_five_categories[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""



