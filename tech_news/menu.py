from tech_news.menu_pack import menu_options
import sys

# Requisito 12


def generate_view_menu():
    print("Selecione uma das opções a seguir:")

    for index, option in enumerate(menu_options.options):
        print(f" {index} - {option[0]};")

    exit_index = len(menu_options.options)
    print(f" {exit_index} - Sair.")

    option_selected = int(input())

    return option_selected if option_selected != exit_index else -1


def analyzer_menu():
    try:
        option_selected = generate_view_menu()

        if option_selected == -1:
            return print("Encerrando script")

        result = menu_options.options[option_selected][1]()
        print(result)
    except ValueError:
        print("Opção inválida")
    except IndexError:
        print("Opção inválida", file=sys.stderr)
