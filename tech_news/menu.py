import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)

"""
Ideia retirada de:
https://www.upgrad.com/blog/how-to-implement-switch-case-functions-in-python/
"""


def option0():
    amount = int(input("Digite quantas notícias serão buscadas:"))
    return get_tech_news(amount)


def option1():
    title = input("Digite o título:")
    return search_by_title(title)


def option2():
    date = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(date)


def option3():
    source = input("Digite a fonte:")
    return search_by_source(source)


def option4():
    category = input("Digite a categoria:")
    return search_by_category(category)


def option5():
    return top_5_news()


def option6():
    return top_5_categories()


def option7():
    return print("Encerrando script\n")


# Requisito 12
def analyzer_menu():

    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )

    switcher = {
        "0": option0,
        "1": option1,
        "2": option2,
        "3": option3,
        "4": option4,
        "5": option5,
        "6": option6,
        "7": option7,
    }

    try:
        result = switcher[option]()
        return result
    except Exception:
        return print("Opção inválida", file=sys.stderr)
