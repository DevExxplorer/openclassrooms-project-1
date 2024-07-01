import requests as req
import csv
from bs4 import BeautifulSoup

def parse_html(url):
    r = req.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def get_number_star(data):
    match data['class'][1]:
        case "One":
            result = 1
        case "Two":
            result = 2
        case "Three":
            result = 3
        case "Four":
            result = 4
        case "Five":
            result = 5
        case _:
            result = "Error"

    return result


def get_info_book(data):
    book = {
        "title": data.h1.string,
        "price": data.find(class_="price_color").string,
        "star_rating": get_number_star(data.find(class_="star-rating")),
        # "description": data.find(id="product_description").find_next_sibling().string,
        "upc": data.find_all('td')[0].string,
        "product_type": data.find_all('td')[1].string,
        "price_excl_tax": data.find_all('td')[2].string,
        "price_incl_tax": data.find_all('td')[3].string,
        "tax": data.find_all('td')[4].string,
        "availability": data.find_all('td')[5].string,
        "number_reviews": data.find_all('td')[6].string,
    }

    return book


def create_csv(data_book):
    with open("book.csv", "w", newline="") as csvfile:
        fieldnames = data_book.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data_book)

