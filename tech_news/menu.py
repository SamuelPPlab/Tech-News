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

MENU_PROMPT = (
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


def zero():
    message = input("Digite quantas notícias serão buscadas: ")
    response = get_tech_news(int(message))
    print(response)


def one():
    message = input("Digite o título: ")
    response = search_by_title(message)
    print(response)


def two():
    message = input("Digite a data no formato aaaa-mm-dd: ")
    response = search_by_date(message)
    print(response)


def three():
    message = input("Digite a fonte: ")
    response = search_by_source(message)
    print(response)


def four():
    message = input("Digite a categoria: ")
    response = search_by_category(message)
    print(response)


def five():
    response = top_5_news()
    print(response)


def six():
    response = top_5_categories()
    print(response)


def seven():
    print("Encerrando script")


DICT = {
    "0": zero,
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": five,
    "6": six,
    "7": seven,
}


def invalid_option(option):
    if not option.isdigit() or int(option) not in range(8):
        print("Opção inválida", file=sys.stderr)
        return True
    return False


def analyzer_menu():
    option = input(MENU_PROMPT)

    if invalid_option(option):
        return

    function = DICT.get(option)
    function()
