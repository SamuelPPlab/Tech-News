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
def create_count_categories_dict(results):
    count_categories_dict = {}
    for result in results:
        categories_list = result["categories"]
        for category in categories_list:
            if category in count_categories_dict:
                count_categories_dict[category] = (
                    count_categories_dict[category] + 1
                )
            else:
                count_categories_dict[category] = 1
    return count_categories_dict


def top_5_categories():
    """Seu código deve vir aqui"""
    results = search_news({})

    count_categories_dict = create_count_categories_dict(results)

    count_categories_sorted_by_key = dict(
        sorted(count_categories_dict.items(), key=lambda x: x[0].lower())
    )
    count_categories_sorted_by_value = sorted(
        count_categories_sorted_by_key.items(),
        key=lambda x: x[1],
        reverse=True,
    )

    top_categories = []
    if len(count_categories_sorted_by_value) <= 5:
        for tupla in count_categories_sorted_by_value:
            top_categories.append(tupla[0])
        return top_categories

    for index in range(5):
        top_categories.append(count_categories_sorted_by_value[index][0])

    return top_categories
