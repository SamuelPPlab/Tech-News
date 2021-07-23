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
    return input('Digite quantas notícias serão buscadas: ')


def handle_selected_option1():
    return input('Digite o título: ')


def handle_selected_option2():
    return input('Digite a data no formato aaaa-mm-dd: ')


def handle_selected_option3():
    return input('Digite a fonte: ')


def handle_selected_option4():
    return input('Digite a categoria: ')


def analyzer_menu():
    option = print_options()

    options = {
        "0": handle_selected_option0,
        "1": handle_selected_option1,
        "2": handle_selected_option2,
        "3": handle_selected_option3,
        "4": handle_selected_option4,
    }

    try:
        result = options[option]()
        print(result)
        return result
    except KeyError:
        print('Opção inválida')
