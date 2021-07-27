from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def get_news():
    quantity = int(input("Digite quantas notícias serão buscadas:"))
    return get_tech_news(quantity)


def get_news_by_title():
    title = input("Digite o título:")
    return search_by_title(title)


def get_news_by_date():
    date = int(input("Digite a data no formato aaaa-mm-dd:"))
    return search_by_date(date)


def get_news_by_source():
    source = input("Digite a fonte:")
    return search_by_source(source)


def get_news_by_category():
    category = input("Digite a categoria:")
    return search_by_category(category)


def quit_script():
    return "Encerrando script"


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    # message = "Selecione uma das opções a seguir:"
    options = [
        "Selecione uma das opções a seguir:",
        " 0 - Popular o banco com notícias;",
        " 1 - Buscar notícias por título;",
        " 2 - Buscar notícias por data;",
        " 3 - Buscar notícias por fonte;",
        " 4 - Buscar notícias por categoria;",
        " 5 - Listar top 5 notícias;",
        " 6 - Listar top 5 categorias;",
        " 7 - Sair."
    ]

    actions = [
        get_news,
        get_news_by_title,
        get_news_by_date,
        get_news_by_source,
        get_news_by_category,
        top_5_news,
        top_5_categories,
        quit_script,
    ]

    # print(message)
    [print(option) for option in options]

    try:
        chosen_option = int(input())
        if 0 <= chosen_option <= 8:
            return print(actions[chosen_option]())
    except ValueError:
        print("Opção inválida")
