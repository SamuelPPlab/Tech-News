from tech_news.database import find_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    try:
        found_news = find_news()
        news = sorted(found_news, key=itemgetter("title"))
        if (len(news) <= 0):
            return news
        if not news:
            return None
    except AssertionError:
        return None
    most_popular_news = sorted(
        news,
        key=lambda item: item["shares_count"] + item["comments_count"],
        reverse=True,
    )[:5]
    return [
        (most_popular_news["title"], most_popular_news["url"])
        for most_popular_news in most_popular_news
    ]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
