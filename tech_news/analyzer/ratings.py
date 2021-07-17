from tech_news.database import find_news


# Requisito 10
def top_5_news():
    found_news = find_news()

    news_list = []
    for news in found_news:
        title = news.get("title")
        url = news.get("url")
        comments_count = news.get("comments_count")
        shares_count = news.get("shares_count")
        popularity = comments_count + shares_count

        news_list.append((title, url, popularity))

    def sort_by_popularity(news):
        (title, url, popularity) = news
        return popularity

    news_list.sort(key=sort_by_popularity, reverse=True)

    filtered_list = []
    counter = 0
    while counter < 5 and counter < len(news_list):
        (title, url, popularity) = news_list[counter]
        filtered_list.append((title, url))
        counter += 1

    return filtered_list


# Requisito 11
def top_5_categories():
    found_news = find_news()

    categories_count = {}
    for news in found_news:
        categories = news.get("categories")
        for category in categories:
            if category not in categories_count:
                categories_count[category] = 0
            categories_count[category] += 1

    categories_count = list(categories_count.items())
    categories_count.sort(key=lambda category: category[0])

    category_list = [category[0] for category in categories_count]

    filtered_list = []
    counter = 0
    while counter < 5 and counter < len(category_list):
        category = category_list[counter]
        filtered_list.append(category)
        counter += 1

    return filtered_list
