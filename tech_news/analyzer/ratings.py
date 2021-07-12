from tech_news.database import find_news, get_collection


def extract_data(data):
    return(data['title'], data['url'])


# Requisito 10
def top_5_news():
    response = find_news()
    result = []
    for data in response:
        result.append(extract_data(data))
    return result[:5]


# Requisito 11
def top_5_categories():
    response = list(get_collection())
    result = []
    for data in response:
        result.append(data)
    return result[:5]


x = top_5_categories()
print(x)