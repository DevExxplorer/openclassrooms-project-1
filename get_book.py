from csv import DictWriter
from book import get_data_book
from requests import get
from bs4 import BeautifulSoup
import os


def make_csv(data):
    data_key = data.keys()
    folder = "one_book"

    if not os.path.exists('csv/' + folder):
        os.makedirs('csv/' + folder)

    with open('csv/' + folder + '/a-light-in-the-attic.csv', "w", newline="") as csvfile:
        writer = DictWriter(csvfile, fieldnames=data_key)
        writer.writeheader()
        writer.writerow(data)


def parse_html(url):
    r = get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def get_book(url=None):
    if not url:
        url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

    html_book = parse_html(url)
    data = get_data_book(html_book, url)

    return data


def save_book():
    data = get_book()
    make_csv(data)
