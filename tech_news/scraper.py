import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        RESPONSE = requests.get(url, timeout=3)
        # print(RESPONSE.content)
        STATUS = RESPONSE.status_code
        if STATUS != 200:
            return None
        HTML = RESPONSE.text
        return HTML
    except requests.Timeout:
        return None


# link = "https://www.tecmundo.com.br/novidades"
# fetch(link)


def handle_shares_count(shares_count_list):
    shares_count = 0
    for count in shares_count_list:
        # print(count.isnumeric())
        if count.isnumeric() is True:
            shares_count = int(count)
    return shares_count


def handle_sumary_elements(summary_list):
    result = ""
    for element in summary_list:
        result += element
    return result


def remove_spaces(element):
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
    # print(new_element)
    return new_element


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


# Requisito 2
def scrape_noticia(html_content):
    SELECTOR = Selector(text=html_content)

    url = SELECTOR.css("head link[rel=canonical]::attr(href)").get()
    title = SELECTOR.css("h1.tec--article__header__title::text").get()
    timestamp = SELECTOR.css("time::attr(datetime)").get()
    writer_text = SELECTOR.css("a.tec--author__info__link::text").get()
    writer = remove_spaces(writer_text)
    shares_count_text = SELECTOR.css("div.tec--toolbar__item::text").get()
    shares_count_list = shares_count_text.split(" ")
    shares_count = handle_shares_count(shares_count_list=shares_count_list)
    comments_count = int(
        SELECTOR.css("button.tec--btn::attr(data-count)").get()
    )
    summary_element_list = SELECTOR.css(
        "div.tec--article__body p:first-child *::text"
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
    print(dict_result)
    return dict_result


# link = "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
# scrape_noticia(fetch(link))


# Requisito 3
def scrape_novidades(html_content):
    SELECTOR = Selector(text=html_content)

    link_list = SELECTOR.css("div.tec--card__info h3 a::attr(href)").getall()
    # print(link_list)
    return link_list


link = "https://www.tecmundo.com.br/novidades"
scrape_novidades(fetch(link))


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
