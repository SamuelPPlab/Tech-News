import requests
import time
import tech_news.scraper_services as scraper

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
    return dict(
        {
            "url": scraper.get_one(
                html_content, 'link[rel="canonical"]::attr("href")'
            ),
            "title": scraper.get_one(
                html_content, 'h1[class="tec--article__header__title"]::text'
            ),
            "timestamp": scraper.get_one(html_content, "time::attr(datetime)"),
            "writer": scraper.cut_blanks_spaces(
                scraper.get_one(
                    html_content, 'a[class="tec--author__info__link"]::text'
                )
            ),
            "shares_count": scraper.extract_shares_count(
                scraper.get_one(
                    html_content, 'div[class="tec--toolbar__item"]::text'
                )
            ),
            "comments_count": int(
                scraper.get_one(
                    html_content, "#js-comments-btn::attr(data-count)"
                )
            ),
            "summary": scraper.extract_summary(
                scraper.get_one(html_content, ".tec--article__body p")
            ),
            "sources": scraper.cut_blanks_spaces_list(
                scraper.get_many(
                    html_content, 'div[class="z--mb-16 z--px-16"] a::text'
                )
            ),
            "categories": scraper.cut_blanks_spaces_list(
                scraper.get_many(html_content, "#js-categories a::text")
            ),
        }
    )


# Requisito 3 class="tec--list__item"
def scrape_novidades(html_content):
    url_list = scraper.get_many(
        html_content,
        'main a[class="tec--card__title__link"]::attr(href)',
    )
    return url_list


# Requisito 4
def scrape_next_page_link(html_content):
    return (
        scraper.get_one(
            html_content,
            'a[class="tec--btn tec--btn--lg tec--btn--primary z--mx-auto z--mt-48"]::attr(href)',
        )
        or None
    )


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
