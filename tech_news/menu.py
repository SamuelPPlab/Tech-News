# Requisito 12

def get_opt_2(option):
    if option == '3':
        return 'Digite a fonte:'
    if option == '4':
        return 'Digite a categoria:'
    return 'Opção inválida'


def get_opt(option):
    if option == '0':
        return 'Digite quantas notícias serão buscadas:'
    if option == '1':
        return 'Digite o título:'
    if option == '2':
        return 'Digite a data no formato aaaa-mm-dd:'
    return get_opt_2(option)


def analyzer_menu():
    initial_message = (
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

    option = input(initial_message)

    return get_opt(option)
