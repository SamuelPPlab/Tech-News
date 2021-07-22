import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_category,
    search_by_date,
    search_by_source,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def index0():
    totalNews = input("Digite quantas notícias serão buscadas: ")
    return get_tech_news(totalNews)


def index1():
    title = input("Digite o título da notícia: ")
    return search_by_title(title)


def index2():
    date = input("Digite a data da notícia: ")
    return search_by_date(date)


def index3():
    source = input("Digite a fonte: ")
    return search_by_source(source)


def index4():
    category = input("Digite a categoria: ")
    return search_by_category(category)


def index5():
    return top_5_news()


def index6():
    return top_5_categories()


def index7():
    return sys.exit()


def analyzer_menu():
    index = input(
        "Selecione uma das opções a seguir:\n"
        + " 0 - Popular o banco com notícias;\n"
        + " 1 - Buscar notícias por título;\n"
        + " 2 - Buscar notícias por data;\n"
        + " 3 - Buscar notícias por fonte;\n"
        + " 4 - Buscar notícias por categoria;\n"
        + " 5 - Listar top 5 notícias;\n"
        + " 6 - Listar top 5 categorias;\n"
        + " 7 - Sair.\n"
    )
    choice = {
        "0": index0,
        "1": index1,
        "2": index2,
        "3": index3,
        "4": index4,
        "5": index5,
        "6": index6,
        "7": index7,
    }

    try:
        result = choice[index]()
        print(result)
        return result
    except KeyError:
        print("Opção inválida")
