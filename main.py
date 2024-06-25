import requests as req
import product
import csv

from bs4 import BeautifulSoup


def parse_data(url):
    r = req.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def create_csv(data_products):
    with open('products.csv', 'w', newline='') as csvfile:
        fieldnames = data_products[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for line_product in data_products:
            writer.writerow(line_product)


def get_data_article_by_href(url, href):
    data_parse = parse_data(url + href)
    return product.get_info_product(data_parse)


def get_data_page(url):
    list_products = []
    data = parse_data(url)

    for i, article in enumerate(data.find_all('article')):
        list_products.append(get_data_article_by_href(url, article.a['href']))

        create_csv(list_products)


get_data_page('https://books.toscrape.com/', data={'key': 'value'})

