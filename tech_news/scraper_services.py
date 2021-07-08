from parsel import Selector


def get_one(base, query):
    selector = Selector(base)
    return selector.css(query).get()


def get_many(base, query):
    selector = Selector(base)
    return selector.css(query).getall()


def cut_blanks_spaces(string):
    return str(string)[1:-1]


def cut_blanks_spaces_list(item_list):
    items = item_list if type(item_list) == "list" else list(item_list)
    return list(map(lambda category: cut_blanks_spaces(category), items))


def extract_shares_count(string):
    numbers = list(filter(lambda letter: str(letter).isnumeric(), string)) or 0
    number = int(
        numbers if str(numbers).isnumeric() else int("".join(numbers))
    )
    return number


def extract_summary(query):
    content_list = "".join(Selector(query).css("*::text").getall())
    return content_list
