import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def handle_function_zero():
    return get_tech_news(int(input("Digite quantas notícias serão buscadas:")))


def handle_function_one():
    return search_by_title(input("Digite o título:"))


def handle_function_two():
    return search_by_date(input("Digite a data no formato aaaa-mm-dd:"))


def handle_function_three():
    return search_by_source(input("Digite a fonte:"))


def handle_function_four():
    return search_by_category(input("Digite a categoria:"))


def handle_function_five():
    return top_5_news()


def handle_function_six():
    return top_5_categories()


def handle_function_seven():
    return print("Encerrando script\n")


# Requisito 12
def analyzer_menu():
    first_menu_options = int(input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    ))

    menu_functions = [
        handle_function_zero,
        handle_function_one,
        handle_function_two,
        handle_function_three,
        handle_function_four,
        handle_function_five,
        handle_function_six,
        handle_function_seven,
    ]

    if first_menu_options < 8:
        return menu_functions[first_menu_options]()
    else:
        sys.stderr.write("Opção inválida\n")


# Lucas Zago Lorena Goes Flavio Sugano
