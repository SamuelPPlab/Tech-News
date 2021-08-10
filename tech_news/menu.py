import sys


OPTIONS = (
    "\n"
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


def switcher(option):
    switch = [
        "Digite quantas notícias serão buscadas:",
        "Digite o título:",
        "Digite a data no formato aaaa-mm-dd:",
        "Digite a fonte:",
        "Digite a categoria:",
    ]
    return switch[option]


def analyzer_menu():
    userInput = input(OPTIONS)
    if not userInput.isdigit() or int(userInput) > 7:
        print("Opção inválida", file=sys.stderr)
    if (int(userInput)) <= 4:
        message = switcher(int(userInput))
        print(message)
    else:
        return
