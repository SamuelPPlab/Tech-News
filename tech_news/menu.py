from sys import stderr

# Requisito 12

menu = [
    "Selecione uma das opções a seguir:",
    " 0 - Popular o banco com notícias;",
    " 1 - Buscar notícias por título;",
    " 2 - Buscar notícias por data;",
    " 3 - Buscar notícias por fonte;",
    " 4 - Buscar notícias por categoria;",
    " 5 - Listar top 5 notícias;",
    " 6 - Listar top 5 categorias;",
    " 7 - Sair.",
]


def option_invalid(option):
    if option in range(5, 8):
        return print("Opção inválida", file=stderr)
    if option not in range(8):
        return print("Opção inválida", file=stderr)


def analyzer_menu():
    try:
        for option in menu:
            print(option)
        user_option = int(input("Digite a opção desejada"))
        option_invalid(user_option)
        searches = {
            0: "Digite quantas notícias serão buscadas:",
            1: "Digite o título:",
            2: "Digite a data no formato aaaa-mm-dd:",
            3: "Digite a fonte:",
            4: "Digite a categoria:",
        }
        return print(searches[user_option])
    except (KeyError, ValueError):
        stderr.write("Opção inválida\n")
