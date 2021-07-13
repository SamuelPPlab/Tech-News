from tech_news.database import find_news


# Requisito 10
def top_5_news():
    all_news = find_news()
    top_five_news = []
    for news in all_news:
        news["total_rate"] = news["shares_count"] + news["comments_count"]
    rated_news = sorted(all_news, key=lambda keys: ("total_rate", "title"))[:5]
    
    for item in rated_news:
        top_five_news.append((item["title"], item["url"]))

    print(top_five_news)
    return top_five_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
