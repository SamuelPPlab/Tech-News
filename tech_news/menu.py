from tech_news.menu_pack import menu_options
import sys

# Requisito 12


def generate_view_menu():
    print("Selecione uma das opções a seguir:")

    for index, option in enumerate(menu_options.options):
        print(f" {index} - {option[0]};")

    exit_index = len(menu_options.options)
    print(f" {exit_index} - Sair.")

    return exit_index


def analyzer_menu():
    exit_index = generate_view_menu()

    try:
        option_selected = int(input())

        if option_selected == exit_index:
            print("Encerrando script")
            return

        result = menu_options.options[option_selected][1]()
        print(result)
    except ValueError or IndexError:
        print("Opção inválida")
    except IndexError:
        print("Opção inválida", file=sys.stderr)
