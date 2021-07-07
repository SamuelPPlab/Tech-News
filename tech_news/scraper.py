import requests


LINK = "https://www.tecmundo.com.br/novidades"


# Requisito 1
def fetch(url):
    REQUEST = requests.get(url)
    print(REQUEST.raise_for_status())
    # print(type(REQUEST.status_code))
    # print(REQUEST.headers["Content-Type"])
    if REQUEST.status_code == 200:
        try:
            HTML = REQUEST.text
            # print(HTML)
            return HTML
        except ValueError:
            print("Deu algum Erro")


fetch(LINK)


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
