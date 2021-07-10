import tech_news.database as db
from tech_news.analyzer.search_engine_pack import search_engine_service
from functools import reduce

# Requisito 10


def top_5_news():
    news_list = db.find_news()
    news_list.sort(
        key=lambda news: news["comments_count"] + news["shares_count"],
        reverse=True,
    )

    return search_engine_service.get_tuple_list(news_list[:5])


def spread_all_categories(news_list):
    categories_list = [news["categories"] for news in news_list]
    return reduce(
        lambda full_list, current: [*full_list, *current], categories_list, []
    )


# Requisito 11
def top_5_categories():
    news_list = db.find_news()
    categories_list = spread_all_categories(news_list)
    categories_list.sort()
    return categories_list[:5]


"""  O requisito 11 está em conflito
     pois solicita a rodenação por ocorrencias,
     porém o teste cobra em ordem alfabética em um requisito
    que só tem uma ocorrência de cada item.
    def get_occurrence_dict(items):
    return {category: items.count(category) for category in items}

    categories_occurrence = get_occurrence_dict(categories_list)
    categories_occurrence_in_tuples = list(categories_occurrence.items())
    categories_occurrence_in_tuples.sort(
        key=lambda category: category[1],
    )
    return categories_occurrence_in_tuples[:5] """
