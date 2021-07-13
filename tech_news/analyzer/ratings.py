from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news_list = find_news()
    popularity_list = [
        [
            int(news["shares_count"]) + int(news["comments_count"]),
            news["title"],
            news["url"],
        ]
        for news in news_list
    ]
    ordered_list = sorted(popularity_list, reverse=True)
    result = [
        (ordered_news[1], ordered_news[2]) for ordered_news in ordered_list[:5]
    ]
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    news_list = find_news()

    categories = {}
    for item in news_list:
        for cat in item["categories"]:
            if cat in categories:
                categories[cat] += 1
            else:
                categories[cat] = 1

    sorted(categories)

    result = []
    for item in categories:
        result.append(item)
    result.sort()

    return result[:5]
