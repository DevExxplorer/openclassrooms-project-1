import requests as req
import product

from bs4 import BeautifulSoup


def parse_data(url):
    r = req.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def get_data_article_by_href(url, href):
    data = parse_data(url + href)
    test = product.get_info_product(data)
    print(test)


def get_data_page(url):
    data = parse_data(url)

    for i, article in enumerate(data.find_all('article')):
        if i == 1:
            get_data_article_by_href(url, article.a['href'])


get_data_page('https://books.toscrape.com/')

