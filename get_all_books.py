
from get_book import parse_html
from get_books_category import save_books_category
from shutil import rmtree
from os import path, mkdir


def get_list_categories():
    categories = []
    categories_html = parse_html('https://books.toscrape.com/index.html')
    nav_list = categories_html.find(class_='nav-list')
    links_list = nav_list.find_all('a')

    for link in links_list:
        categories.append(link.get('href').split('/')[-2])

    return categories


def save_all_books():
    categories = get_list_categories()

    # Delete folder for delete old images and category folder and create new folder
    if path.isdir('images'):
        rmtree('images')

    mkdir('images/')

    for category in categories:
        if category != 'books_1':
            name_category = category.split('_')
            mkdir('images/' + name_category[0])
            save_books_category(category, True)