from sys import stderr

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


# Requisito 12
def analyzer_menu():
    try:
        for opção in menu:
            print(opção)

        retorno = int(input("Digite o número da opção desejada: "))

        if retorno not in range(8):
            return print("Opção inválida", file=stderr)

        retornos = {
            0: "Digite quantas notícias serão buscadas:",
            1: "Digite o título:",
            2: "Digite a data no formato aaaa-mm-dd:",
            3: "Digite a fonte:",
            4: "Digite a categoria:",
        }
        print(retornos[retorno])

    except (KeyError, ValueError):
        stderr.write("Opção inválida\n")
