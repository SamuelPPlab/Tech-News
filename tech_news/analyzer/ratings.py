from tech_news.database import find_news


def extract_data(data):
    return(data['title'], data['url'])


# Requisito 10
def top_5_news():
    response = find_news()
    result = []
    for data in response:
        result.append(extract_data(data))
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
