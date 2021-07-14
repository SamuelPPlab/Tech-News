from tech_news.database import find_news

top_news = []


def order(list_news):
    new_array = []
    list_news.sort(
        key=lambda item: (item["popularity"], item["title"]), reverse=True)
    for item in range(5):
        new_array.append(top_news[item])
    return new_array


def to_extract(list_news):
    array = [(item['title'], item['url']) for item in list_news]
    return array


def remove_values_repeated(array_list):
    list_news = []
    for item in array_list:
        if (item not in list_news):
            list_news.append(item)
    list_news.sort()
    return list_news


# Requisito 10
def top_5_news():
    list_news = find_news()

    if(len(list_news) == 0):
        return list_news

    for news in list_news:
        popularity = news['shares_count'] + news['comments_count']
        news["popularity"] = popularity
        top_news.append(news)

    new_array = order(top_news)
    extract = to_extract(new_array)

    return remove_values_repeated(extract)


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
