import sys


OPTIONS = (
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


def analyzer_menu():
    userInput = input(OPTIONS)
    if (int(userInput) > 7):
        print("Opção inválida", file=sys.stderr)
    if (int(userInput) == 0):
        print("Digite quantas notícias serão buscadas:")
    if (int(userInput) == 1):
        print("Digite o título:")
    if (int(userInput) == 2):
        print("Digite a data no formato aaaa-mm-dd:")
    if (int(userInput) == 3):
        print("Digite a fonte:")
    if (int(userInput) == 4):
        print("Digite a categoria:")
