from tech_news.database import search_news


# Requisito 10
def put_popularity(results):
    for result in results:
        popularity = result["shares_count"] + result["comments_count"]
        result["popularity"] = popularity
    return results


def top_5_news():
    """Seu código deve vir aqui"""
    results = search_news({})

    results = put_popularity(results)
    # for result in results:
    #     popularity = result["shares_count"] + result["comments_count"]
    #     result["popularity"] = popularity

    results.sort(key=lambda x: x["title"])

    def get_my_pop_key(obj):
        return obj["popularity"]

    results.sort(key=get_my_pop_key, reverse=True)

    result_tupla = []
    if len(results) <= 5:
        for result in results:
            tupla = (result["title"], result["url"])
            result_tupla.append(tupla)
        return result_tupla

    for i in range(5):
        tupla = (results[i]["title"], results[i]["url"])
        result_tupla.append(tupla)

    return result_tupla


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
