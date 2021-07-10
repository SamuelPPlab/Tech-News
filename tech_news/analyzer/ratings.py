from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    for new in news:
        new["popularity"] = new["comments_count"] + new["shares_count"]
    sorted_news = sorted(news, key=lambda n: n["popularity"], reverse=True)
    top_5 = [new for new in sorted_news[:5]]
    return [(new["title"], new["url"]) for new in top_5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
