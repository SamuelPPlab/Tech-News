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


def get_attributes_of(base):
    return dict(
        {
            "url": get_one(base, 'link[rel="canonical"]::attr("href")'),
            "title": get_one(
                base, 'h1[class="tec--article__header__title"]::text'
            ),
            "timestamp": get_one(base, "time::attr(datetime)"),
            "writer": cut_blanks_spaces(
                get_one(base, 'a[class="tec--author__info__link"]::text')
            ),
            "shares_count": extract_shares_count(
                get_one(base, 'div[class="tec--toolbar__item"]::text')
            ),
            "comments_count": int(
                get_one(base, "#js-comments-btn::attr(data-count)")
            ),
            "summary": extract_summary(get_one(base, ".tec--article__body p")),
            "sources": cut_blanks_spaces_list(
                get_many(base, 'div[class="z--mb-16 z--px-16"] a::text')
            ),
            "categories": cut_blanks_spaces_list(
                get_many(base, "#js-categories a::text")
            ),
        }
    )
