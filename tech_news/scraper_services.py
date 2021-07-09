import re
from parsel import Selector


def get_one(base, query):
    selector = Selector(base)
    return selector.css(query).get()


def get_one_xpath(base, query):
    selector = Selector(base)
    return selector.xpath(query).get()


def get_many(base, query):
    selector = Selector(base)
    return selector.css(query).getall()


def get_many_xpath(base, query):
    selector = Selector(base)
    return selector.xpath(query).getall()


def cut_blanks_spaces(string):
    return str(string)[1:-1]


def cut_blanks_spaces_list(item_list):
    items = item_list if type(item_list) == "list" else list(item_list)
    return list(map(lambda category: cut_blanks_spaces(category), items))


def extract_number(string):
    if not isinstance(string, str):
        return 0
    return int(re.sub(r"\D", "", string))


def extract_summary(query):
    content_list = "".join(Selector(query).css("*::text").getall())
    return content_list
