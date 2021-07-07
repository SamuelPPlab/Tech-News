from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_list = find_news()
    popularity_list = sorted(
        news_list,
        key=lambda x: x["shares_count"] + x["comments_count"],
        reverse=True,
    )
    return ([(news["title"], news["url"]) for news in popularity_list[:5]])


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
