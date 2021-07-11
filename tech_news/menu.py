import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import (
    top_5_news,
    top_5_categories,
)


def condition_7(response, value, message, number):
    if response == number and value == number:
        print(message)
        return True
    return False


def condition_5_and_6(response, value, function, number):
    if response == number and value == number:
        print(function())
        return True
    return False


def conditional_option(response, value, message, function):
    result = False
    result = condition_7(response, value, message, "7")
    if result is not True:
        result = condition_5_and_6(response, value, function, "5")
    if result is not True:
        result = condition_5_and_6(response, value, function, "6")
    if result is not True and response == value:
        result = input(message)
        if result.isnumeric() is True:
            function(int(result))
            result = True
            return result
        else:
            print(function(result))
            result = True
            return result
    return result


# Requisito 12
def analyzer_menu():
    menu_questions = (
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )

    list_values = [
        {
            "number": "0",
            "message": "Digite quantas notícias serão buscadas:",
            "function": get_tech_news,
        },
        {
            "number": "1",
            "message": "Digite o título:",
            "function": search_by_title,
        },
        {
            "number": "2",
            "message": "Digite a data no formato aaaa-mm-dd:",
            "function": search_by_date,
        },
        {
            "number": "3",
            "message": "Digite a fonte:",
            "function": search_by_source,
        },
        {
            "number": "4",
            "message": "Digite a categoria:",
            "function": search_by_category,
        },
        {"number": "5", "message": "", "function": top_5_news},
        {"number": "6", "message": "", "function": top_5_categories},
        {"number": "7", "message": "Encerrando script", "function": ""},
    ]

    response = input(menu_questions)
    fail = False

    for value in list_values:
        result = conditional_option(
            response,
            value["number"],
            value["message"],
            value["function"],
        )
        if result is True:
            fail = False
            break
        else:
            fail = True

    if fail is True:
        print("Opção inválida", file=sys.stderr)


# analyzer_menu()
