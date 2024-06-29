import requests as req
import product
import csv
import os
from bs4 import BeautifulSoup

"""
Permet de parser le code HTML récupérer avec request
"""


def parse_data(url):
    r = req.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


"""
Création d'un fichier csv
"""


def create_csv(books_list):
    with open("products.csv", "w", newline="") as csvfile:
        fieldnames = books_list[0][0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for line_product in books_list:
            writer.writerows(line_product)


"""
Récupere les données HTML d'un produit en fonction de son url
"""


def get_data_article_by_href(href):
    data_parse = parse_data('https://books.toscrape.com/catalogue/' + href)
    return product.get_info_product(data_parse)


"""

"""


def get_data_page(url):
    list_products = []
    data = parse_data(url)

    for i, article in enumerate(data.find_all('article')):
        list_products.append(get_data_article_by_href(article.a['href']))
    return list_products


def check_next_page(url):
    next_page = False
    data = parse_data(url)
    if data.find(class_="next"):
        next_page = True

    return next_page


next_page = True
page = 1
books_list = []

while next_page:
    url = 'https://books.toscrape.com/catalogue/page-' + str(page) + '.html'
    books_list.append(get_data_page(url))

    if check_next_page(url):
        page += 1
    else:
        next_page = False

# create_csv(books_list)

