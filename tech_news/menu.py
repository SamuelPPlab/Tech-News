import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)


# Requisito 12
def print_menu():
    print("Selecione uma das opções a seguir:")
    print(" 0 - Popular o banco com notícias;")
    print(" 1 - Buscar notícias por título;")
    print(" 2 - Buscar notícias por data;")
    print(" 3 - Buscar notícias por fonte;")
    print(" 4 - Buscar notícias por categoria;")
    print(" 5 - Listar top 5 notícias;")
    print(" 6 - Listar top 5 categorias;")
    print(" 7 - Sair.")


def analize_option(option):
    switcher = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a fonte:",
        "4": "Digite a categoria:",
    }
    return switcher.get(option)


def handle_options_0_to_1(option, info):
    try:
        if option == "0":
            return get_tech_news(int(info))
    except ValueError:
        return get_tech_news(0)

    if option == "1":
        return search_by_title(info)


def handle_options_2_to_5(option, info):
    if option == "2":
        return search_by_date(info)

    if option == "3":
        return search_by_source(info)

    if option == "4":
        return search_by_category(info)

    if option == "5":
        return top_5_news()


def handle_options_6_to_7(option):
    if option == "6":
        return top_5_categories()

    if option == "7":
        return "Encerrando script"


def analize_info(option, info):
    if option in ["0", "1"]:
        return handle_options_0_to_1(option, info)

    if option in ["2", "3", "4", "5"]:
        return handle_options_2_to_5(option, info)

    if option in ["6", "7"]:
        return handle_options_6_to_7(option)


def analyzer_menu():
    """Seu código deve vir aqui"""
    print_menu()
    option = input()

    if option not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
        sys.stderr.write("Opção inválida\n")
        print(sys.stderr)
        return

    if option in ["1", "2", "3", "4"]:
        info = input(analize_option(option))
        print(analize_info(option, info))
    else:
        print(analize_info(option, info=""))
