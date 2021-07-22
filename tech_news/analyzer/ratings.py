from tech_news.database import find_news


# https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
# Mario F e Boris
# Gleison e Carol
# Requisito 10
def top_5_news():
    response = find_news()

    if len(response) == 0:
        return response

    news_list_with_order = []
    for news in response:
        news['order'] = int(news['shares_count']) + int(news['comments_count'])
        news_list_with_order.append(news)

    sorted_list = sorted(
        news_list_with_order, key=lambda curr_key: (
            curr_key['title'], curr_key['order']
        )
    )[:5]

    return [(news['title'], news['url']) for news in sorted_list]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
