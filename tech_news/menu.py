from sys import exit
from tech_news import scraper
from tech_news.analyzer import search_engine, ratings


def print_options():
    return input(
        'Selecione uma das opções a seguir:\n'
        + ' 0 - Popular o banco com notícias;\n'
        + ' 1 - Buscar notícias por título;\n'
        + ' 2 - Buscar notícias por data;\n'
        + ' 3 - Buscar notícias por fonte;\n'
        + ' 4 - Buscar notícias por categoria;\n'
        + ' 5 - Listar top 5 notícias;\n'
        + ' 6 - Listar top 5 categorias;\n'
        + ' 7 - Sair.\n'
    )


def handle_selected_option0():
    amount = input('Digite quantas notícias serão buscadas: ')
    result = scraper.get_tech_news(amount)
    print(result)
    return result


def handle_selected_option1():
    title = input('Digite o título: ')
    result = search_engine.search_by_title(title)
    print(result)
    return result


def handle_selected_option2():
    date = input('Digite a data no formato aaaa-mm-dd: ')
    result = search_engine.search_by_date(date)
    print(result)
    return result


def handle_selected_option3():
    result = input('Digite a fonte: ')
    return search_engine.search_by_source(result)


def handle_selected_option4():
    category = input('Digite a categoria: ')
    result = search_engine.search_by_category(category)
    print(result)
    return result


def handle_selected_option5():
    result = ratings.top_5_news()
    print(result)
    return result


def handle_selected_option6():
    result = ratings.top_5_categories()
    print(result)
    return result


def handle_selected_option7():
    return exit('Encerrando script\n')


def analyzer_menu():
    option = print_options()

    options = {
        "0": handle_selected_option0,
        "1": handle_selected_option1,
        "2": handle_selected_option2,
        "3": handle_selected_option3,
        "4": handle_selected_option4,
        "5": handle_selected_option5,
        "6": handle_selected_option6,
        "7": handle_selected_option7,
    }

    try:
        result = options[option]()
        print(result)
        return result
    except KeyError:
        print('Opção inválida\n')
