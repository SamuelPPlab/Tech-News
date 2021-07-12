from tech_news.database import create_news
import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(html_content)
    # https://qastack.com.br/programming/7524585/how-do-i-get-the-information-from-a-meta-tag-with-javascript
    url = selector.css("meta[property='og:url']::attr(content)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = selector.css(".tec--author__info__link::text").get()
    shares_count = selector.css(".tec--toolbar__item::text").get()
    comments_count = selector.css("#js-comments-btn::attr(data-count)").get()
    summary = selector.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    categories = selector.css("#js-categories .tec--badge::text").getall()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip() if writer is not None else None,
        "shares_count": int(
            shares_count[:2].strip() if shares_count is not None else 0
        ),
        "comments_count": int(
            comments_count.strip() if comments_count is not None else 0
        ),
        "summary": "".join(summary),
        "sources": [source.strip() for source in sources],
        "categories": [categorie.strip() for categorie in categories],
    }


# Requisito 3
def scrape_novidades(html_content):
    selector = Selector(html_content)
    urls = selector.css("h3 .tec--card__title__link::attr(href)").getall()
    return urls


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next = selector.css(".tec--btn--lg::attr(href)").get()
    return next


# Requisito 5 (Fonte: Call com Anderson, Emerson e Zezo,  )
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    links = []
    # lista de links
    news = []
    # lista de noticias
    while len(links) < amount:
        # a intenção aqui é utilizar o tamanho da lista de links para saber se
        # é necessario ou não buscar novos links
        content_html = fetch(url)
        # buscando html da pagina principal
        list_url = scrape_novidades(content_html)
        # obtendo urls das noticias da pagina
        url = scrape_next_page_link(content_html)
        # alterando o valor de url (linha 67), para que na proxima interação
        # do while, ele busque novos links
        links += list_url
        # adicionando os urls na lista de links, e uma vez
        # que já possua mais links que a quantidade passada (amount), o laço
        # se encerra

    for list in links[:amount]:
        # Tendo a lista de links, é feito um laço na lista de links
        # utilizando somente a quantidade passada (amount), sacada do Anderson
        news.append(scrape_noticia(fetch(list)))
        # a noticia é adicionada a lista de noticias
    create_news(news)
    # a lista de noticias é salva no bd
    return news
