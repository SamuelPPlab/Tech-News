# Requisito 12
import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)

MENU_OPTIONS = (
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


def option_zero():
    message = input("Digite quantas notícias serão buscadas: ")
    response = get_tech_news(int(message))
    print(response)


def option_one():
    message = input("Digite o título: ")
    response = search_by_title(message)
    print(response)


def option_two():
    message = input("Digite a data no formato aaaa-mm-dd: ")
    response = search_by_date(message)
    print(response)


def option_three():
    message = input("Digite a fonte: ")
    response = search_by_source(message)
    print(response)


def option_four():
    message = input("Digite a categoria: ")
    response = search_by_category(message)
    print(response)


def option_five():
    response = top_5_news()
    print(response)


def option_six():
    response = top_5_categories()
    print(response)


def option_seven():
    print("Encerrando script")


FUNCTION_DICT = {
    "0": option_zero,
    "1": option_one,
    "2": option_two,
    "3": option_three,
    "4": option_four,
    "5": option_five,
    "6": option_six,
    "7": option_seven,
}


def invalid_option(option):
    if not option.isdigit() or int(option) not in range(8):
        print("Opção inválida", file=sys.stderr)
        return True
    return False


def analyzer_menu():
    option = input(MENU_OPTIONS)

    if invalid_option(option):
        return

    function = FUNCTION_DICT.get(option)
    function()
