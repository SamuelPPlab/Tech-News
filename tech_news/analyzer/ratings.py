from tech_news.database import find_news


# Requisito 10
def top_5_news():
    all_news = find_news()

    news_array = []
    for news in all_news:
        title = news.get("title")
        url = news.get("url")
        comments_count = news.get("comments_count")
        shares_count = news.get("shares_count")
        top_news = comments_count + shares_count

        news_array.append((title, url, top_news))

    def sort_top_news(news):
        (title, url, top_news) = news
        return top_news

    news_array.sort(key=sort_top_news, reverse=True)

    filtered_news = []
    counter = 0
    while counter < 5 and counter < len(news_array):
        (title, url, top_news) = news_array[counter]
        filtered_news.append((title, url))
        counter += 1

    return filtered_news


# Requisito 11
def top_5_categories():
    all_news = find_news()

    categories_counter = {}
    for news in all_news:
        categories = news.get("categories")
        for category in categories:
            if category not in categories_counter:
                categories_counter[category] = 0
            categories_counter[category] += 1

    categories_counter = list(categories_counter.items())
    categories_counter.sort(key=lambda category: category[0])

    categories_list = [category[0] for category in categories_counter]

    filtered_news = []
    counter = 0
    while counter < 5 and counter < len(categories_list):
        category = categories_list[counter]
        filtered_news.append(category)
        counter += 1

    return filtered_news
