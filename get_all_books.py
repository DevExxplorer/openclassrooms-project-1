
import get_book
import get_books_category
import shutil
import os


def get_list_categories():
    categories = []
    categories_html = get_book.parse_html('https://books.toscrape.com/index.html')
    nav_list = categories_html.find(class_='nav-list')
    links_list = nav_list.find_all('a')

    for link in links_list:
        categories.append(link.get('href').split('/')[-2])

    return categories


def save_all_books():
    categories = get_list_categories()

    # Delete folder for delete old images and category folder and create new folder
    if os.path.isdir('images'):
        shutil.rmtree('images')

    os.mkdir('images/')

    for category in categories:
        if category != 'books_1':
            os.mkdir('images/' + category)
            get_books_category.save_books(category, True)