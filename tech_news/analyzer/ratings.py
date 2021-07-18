from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_list = find_news()
    popularity_result = [
        [
            int(news["shares_count"]) + int(news["comments_count"]),
            news["title"],
            news["url"],
        ]
        for news in news_list
    ]
    popularity_order = sorted(popularity_result, reverse=True)
    result = [(ordered[1], ordered[2]) for ordered in popularity_order[:5]]
    return result


# Requisito 11
def top_5_categories():
    news_list = find_news()
    categories_result_list = []
    if len(news_list) > 0:
        for news in news_list:
            categories_result_list.extend(news["categories"])
    else:
        return []
    categories_result_list.sort()
    return categories_result_list[:5]
