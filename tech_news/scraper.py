from parsel import Selector
import requests
import time


def attribute_in(base):
    selector = Selector(base)

    def get_one(query):
        attribute = selector.css(query).get()
        return attribute

    def get_many(query):
        attribute = selector.css(query).getall()
        return attribute

    def cut_blanks_spaces(string):
        return str(string)[1:-1]

    def get_summary(query):
        p = selector.css(query).get()
        content_list = "".join(Selector(p).css("*::text").getall())
        return content_list

    def get_writer(query):
        return cut_blanks_spaces(get_one(query))

    def get_shares_count(query):
        numbers = (
            list(filter(lambda letter: str(letter).isnumeric(), query)) or 0
        )
        number = int(
            numbers if str(numbers).isnumeric() else int("".join(numbers))
        )
        return number

    def get_sources(query):
        sources = map(
            lambda source: cut_blanks_spaces(source), get_many(query)
        )
        return list(sources)

    def get_comments_count(query):
        return int(get_one(query))

    def get_categories(query):
        categories = map(
            lambda category: cut_blanks_spaces(category), get_many(query)
        )
        return list(categories)

    return {
        "get_one": get_one,
        "get_summary": get_summary,
        "get_writer": get_writer,
        "get_shares_count": get_shares_count,
        "get_sources": get_sources,
        "get_many": get_many,
        "get_comments_count": get_comments_count,
        "get_categories": get_categories,
    }


def scratch_attributes_to(url):
    response = requests.get(url, timeout=3).text

    title = attribute_in(response)["get_one"](
        'h1[class="tec--article__header__title"]::text'
    )
    timestamp = attribute_in(response)["get_one"]("time::attr(datetime)")
    writer = attribute_in(response)["get_writer"](
        'a[class="tec--author__info__link"]::text'
    )
    shares_count = attribute_in(response)["get_shares_count"](
        'div[class="tec--toolbar__item"]::text'
    )

    comments_count = attribute_in(response)["get_comments_count"](
        "#js-comments-btn::attr(data-count)"
    )
    summary = attribute_in(response)["get_summary"](".tec--article__body p")

    sources = attribute_in(response)["get_sources"](
        'div[class="z--mb-16 z--px-16"] a::text'
    )

    categories = attribute_in(response)["get_categories"](
        "#js-categories a::text"
    )
    return dict(
        {
            "url": url,
            "title": title,
            "timestamp": timestamp,
            "writer": writer,
            "shares_count": shares_count,
            "comments_count": comments_count,
            "summary": summary,
            "sources": sources,
            "categories": categories,
        }
    )


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        return response.text if response.status_code == 200 else None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    url_list = attribute_in(html_content)["get_many"](
        'div[class="tec--card__info"] a::attr(href)'
    )
    attributes_list = list(
        map(lambda url: scratch_attributes_to(url), url_list)
    )
    return attributes_list


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
