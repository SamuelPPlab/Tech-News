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


def analize_info(option, info):
    try:
        if option == "0":
            result = get_tech_news(int(info))
    except ValueError:
        result = get_tech_news(0)

    if option == "1":
        result = search_by_title(info)

    if option == "2":
        result = search_by_date(info)

    if option == "3":
        result = search_by_source(info)

    if option == "4":
        result = search_by_category(info)

    if option == "5":
        result = top_5_news()

    if option == "6":
        result = top_5_categories()

    if option == "7":
        result = "Encerrando script"

    return result


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
