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


def analyzer_menu():
    menu = {
        "0": "Digite quantas notícias serão buscadas:",
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a fonte:",
        "4": "Digite a categoria:",
    }

    menu_options = (
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

    option = input(menu_options)

    if not option.isdigit() or int(option) not in range(8):
        print("Opção inválida", file=sys.stderr)
        return

    message = menu.get(option)

    if option == "0":
        input_data = input(message)
        response = get_tech_news(int(input_data))
        print(response)
        return response
    elif option == "1":
        input_data = input(message)
        response = search_by_title(input_data)
        print(response)
        return response
    elif option == "2":
        input_data = input(message)
        response = search_by_date(input_data)
        print(response)
        return response
    elif option == "3":
        input_data = input(message)
        response = search_by_source(input_data)
        print(response)
        return response
    elif option == "4":
        input_data = input(message)
        response = search_by_category(input_data)
        print(response)
        return response
    elif option == "5":
        response = top_5_news()
        print(response)
        return response
    elif option == "6":
        response = top_5_categories()
        print(response)
        return response
    elif option == "7":
        print("Encerrando script")
