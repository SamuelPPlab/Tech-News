from tech_news.database import (
    find_news,
)


# Requisito 10
def sort_by_field(news, filter):
    result = []
    order = 1
    ordered = sorted(news, key=lambda k: k[filter], reverse=True)
    for item in ordered:
        new_item = (item['title'], item['url'])
        result.append(new_item)
        order += 1
    return result[0:5]


def top_5_news():
    """Seu código deve vir aqui"""
    news_list = find_news()
    result = []

    if news_list is None:
        return result
    else:
        for new in news_list:
            share = new['shares_count']
            comment = new['comments_count']
            popularity = share + comment
            new['popularity'] = popularity
    return sort_by_field(news_list, 'popularity')


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    max = 5
    news_list = find_news()
    result = []
    if news_list is None:
        return result
    else:
        for new in news_list:
            categgory_item = sorted(new['categories'])
            [result.append(item) for item in categgory_item]
    return sorted(result)[:max]
