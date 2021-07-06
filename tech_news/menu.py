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


def analyzer_menu():
    """Seu código deve vir aqui"""
    print_menu()
    option = input()

    print(analize_option(option))

    if option not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
        print("Opção inválida")
