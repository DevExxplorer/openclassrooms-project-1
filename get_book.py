import csv
import book
import requests as req
from bs4 import BeautifulSoup


def make_csv(data):
    data_key = data.keys()

    with open('csv/book_a-light-in-the-attic_1000.csv', "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_key)
        writer.writeheader()
        writer.writerow(data)


def parse_html(url):
    r = req.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def get_book(url=None):
    if not url:
        url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

    html_book = parse_html(url)
    data = book.get_data_book(html_book)

    return data


def save_book():
    data = get_book()
    make_csv(data)
