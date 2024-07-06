import csv
import get_book
import re
import requests


def get_slug_with_title(title):
    title = title.lower().strip()
    title = re.sub(r'[^\w\s-]', '', title)
    title = re.sub(r'[-\s]+', '-', title)
    return title


def download_img(img, title, category):
    f = open('images/' + category + '/' + get_slug_with_title(title) + '.jpg', 'wb')
    f.write(requests.get(img).content)
    f.close()


def make_csv(data, category_name):
    data_key = data[0].keys()
    with open('csv/' + category_name + '.csv', "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_key)
        writer.writeheader()
        writer.writerows(data)


def check_next_page(url):
    next_page = False
    data = get_book.parse_html(url)

    if data.find(class_="next"):
        next_page = True

    return next_page


def save_books(category, all_category=False):
    data = []
    next_p = True
    page = 1

    while next_p:
        path = 'index' if page == 1 else 'page-' + str(page)
        url = 'https://books.toscrape.com/catalogue/category/books/' + category + '/' + path + '.html'
        categories = get_book.parse_html(url)

        for article in categories.find_all('article'):
            link = article.find_all('a')[0]
            href = link.get('href')
            path_name = href.split('../')
            books = get_book.get_book('https://books.toscrape.com/catalogue/' + path_name[-1])
            data.append(books)

            if all_category:
                download_img(books['img'], books['title'], category)

        if check_next_page(url):
            page += 1
        else:
            next_p = False

    make_csv(data, category)


