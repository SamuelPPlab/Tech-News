import requests
import time
import math

from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        RESPONSE = requests.get(url, timeout=3)
        STATUS = RESPONSE.status_code
        if STATUS != 200:
            return None
        HTML = RESPONSE.text
        return HTML
    except requests.Timeout:
        return None


# link = "https://www.tecmundo.com.br/novidades"
# fetch(link)


def remove_spaces(element):
    if element is not None:
        element_list = element.split(" ")
        new_element = ""
        for item in element_list:
            if item == element_list[len(element_list) - 2]:
                new_element += item
            elif (
                item != element_list[0]
                and item != element_list[len(element_list) - 1]
            ):
                new_element += item + " "
        return new_element
    return element


def handle_shares_count(shares_count_text):
    if shares_count_text is not None:
        shares_count_list = shares_count_text.split(" ")
        shares_count = 0
        for count in shares_count_list:
            if count.isnumeric() is True:
                shares_count = int(count)
        return shares_count
    return 0


def handle_sumary_elements(summary_list):
    result = ""
    for element in summary_list:
        result += element
    return result


def handle_category_elements(category_list):
    result = []
    for element in category_list:
        if element != " ":
            new_element = remove_spaces(element=element)
            result.append(new_element)
    return result


def handle_source_elements(source_list):
    result = []
    for element in source_list:
        if element != " ":
            new_element = remove_spaces(element=element)
            result.append(new_element)
    return result


def handle_writer_requests(SELECTOR):
    selector_list_css = [
        "#js-author-bar > div > p.z--m-none.z--truncate.z--font-bold > "
        "a::text",
        ".tec--author__info__link::text",
    ]
    writer_text = None

    for select in selector_list_css:
        if writer_text is None:
            writer_text = SELECTOR.css(select).get()

    if writer_text is not None:
        return writer_text.strip()
    return ""


def handle_comments_count_requests(SELECTOR):
    selector_list_css = [
        "#js-comments-btn::attr(data-count)",
    ]
    comments_count = None

    for select in selector_list_css:
        if comments_count is None:
            comments_count = SELECTOR.css(select).get()

    if comments_count is not None and comments_count.isnumeric() is True:
        return int(comments_count)
    return 0


def handle_title_requests(SELECTOR):
    selector_list_css = [
        "#js-article-title::text",
        "h1.tec--article__header__title::text",
        "h1#js-article-title::text",
    ]
    title = None

    for select in selector_list_css:
        if title is None:
            title = SELECTOR.css(select).get()

    if title is not None:
        return title
    return ""


# Requisito 2
def scrape_noticia(html_content):
    SELECTOR = Selector(text=html_content)

    url = SELECTOR.css("head link[rel=canonical]::attr(href)").get()
    title = handle_title_requests(SELECTOR=SELECTOR)
    timestamp = SELECTOR.css("time::attr(datetime)").get()
    writer = handle_writer_requests(SELECTOR=SELECTOR)
    shares_count_text = SELECTOR.css("div.tec--toolbar__item::text").get()
    shares_count = handle_shares_count(shares_count_text=shares_count_text)
    comments_count = handle_comments_count_requests(SELECTOR=SELECTOR)
    summary_element_list = SELECTOR.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    summary = handle_sumary_elements(summary_list=summary_element_list)
    sources_list = SELECTOR.css("div.z--mb-16 div *::text").getall()
    sources = handle_source_elements(source_list=sources_list)
    categories_element_list = SELECTOR.css(
        "div#js-categories *::text"
    ).getall()
    categories = handle_category_elements(categories_element_list)

    dict_result = {
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
    return dict_result


# link = "https://www.tecmundo.com.br/minha-serie/"
# "215302-she-hulk-renee-elise-goldsberry-entra-elenco-serie.htm"
# scrape_noticia(fetch(link))


# Requisito 3
def scrape_novidades(html_content):
    SELECTOR = Selector(text=html_content)

    link_list = SELECTOR.css("div.tec--card__info h3 a::attr(href)").getall()
    return link_list


# link = "https://www.tecmundo.com.br/novidades"
# scrape_novidades(fetch(link))


# Requisito 4
def scrape_next_page_link(html_content):
    try:
        selector = Selector(text=html_content)
        link_next_page = selector.css("a.tec--btn::attr(href)").get()
        return link_next_page
    except ValueError:
        return None


# link = "https://www.tecmundo.com.br/novidades"
# scrape_next_page_link(fetch(link))


def request_amount_less_twenty(html_base, amount, count_value, result_value):
    print("amount menor que 20")
    result = result_value
    count = count_value
    link_news_page = scrape_novidades(html_base)
    for index in range(amount):
        html_new = fetch(link_news_page[index])
        dict_new = scrape_noticia(html_new)
        result.append(dict_new)
        count += 1
        print(count, dict_new["title"], "-", dict_new["writer"])
    return {"result": result, "count": count}


def request_number_of_news_less_twenty(
    html_base, number_of_news, count_value, result_value
):
    print("number_of_news menor que 20")
    result = result_value
    count = count_value
    link_news_page = scrape_novidades(html_base)
    for index in range(number_of_news):
        html_new = fetch(link_news_page[index])
        dict_new = scrape_noticia(html_new)
        result.append(dict_new)
        count += 1
        print(count, dict_new["title"], "-", dict_new["writer"])
    return {"result": result, "count": count}


def request_amount_than_twenty(
    html_base, number_of_news_value, count_value, result_value
):
    print("amount maior que 20")
    result = result_value
    count = count_value
    number_of_news = number_of_news_value
    link_news_page = scrape_novidades(html_base)
    for link in link_news_page:
        html_new = fetch(link)
        dict_new = scrape_noticia(html_new)
        result.append(dict_new)
        number_of_news -= 1
        count += 1
        print(count, dict_new["title"], "-", dict_new["writer"])
    return {"result": result, "count": count, "number_of_news": number_of_news}


def requests_loops_links_news(
    amount, html_base, result_value, news_number, count_value
):
    result = result_value
    count = count_value
    number_of_news = news_number

    if amount <= 20 and html_base is not None:
        request = request_amount_less_twenty(html_base, amount, count, result)
        result = request["result"]
        count = request["count"]
    elif number_of_news <= 20 and html_base is not None:
        request = request_number_of_news_less_twenty(
            html_base, number_of_news, count, result
        )
        result = request["result"]
        count = request["count"]
    elif amount > 20 and html_base is not None:
        request = request_amount_than_twenty(
            html_base, number_of_news, count, result
        )
        result = request["result"]
        count = request["count"]
        number_of_news = request["number_of_news"]
    return {"result": result, "number_of_news": number_of_news}


# Requisito 5
def get_tech_news(amount):
    url_base = "https://www.tecmundo.com.br/novidades"
    html_base = fetch(url_base)
    result = []
    count = 0

    if amount <= 20:
        list_dicts = requests_loops_links_news(
            amount, html_base, result, amount, count
        )
        result = list_dicts["result"]
    else:
        number_pages = math.ceil(amount / 20)
        number_of_news = amount
        for _ in range(number_pages):
            # print("LOOP PAGES")
            # print("NUMBER OF NEWS", number_of_news)
            if number_of_news <= 20:
                list_dicts = requests_loops_links_news(
                    amount, html_base, result, number_of_news, count
                )
                result = list_dicts["result"]
            else:
                list_dicts = requests_loops_links_news(
                    amount, html_base, result, number_of_news, count
                )
                result = list_dicts["result"]
                number_of_news = list_dicts["number_of_news"]
                # Atualizar HTML com a nova página
                next_link = scrape_next_page_link(html_base)
                html_base = fetch(next_link)
    print("Tamanho da lista", len(result))
    create_news(result)
    return result


# get_tech_news(5)
