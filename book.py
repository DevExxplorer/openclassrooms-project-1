from re import search


def get_number_star(data):
    matching_data = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    return matching_data.get(data['class'][1], "Error")


def get_url_img(data):
    carousel_div = data.find(class_="carousel-inner")
    img_html = carousel_div.find('img')
    src_img = img_html.get('src').split('../..')
    return 'https://books.toscrape.com' + src_img[1]


def category_product(data):
    breadcrumb_ul = data.find('ul', class_='breadcrumb')
    breadcrumb_li = breadcrumb_ul.find_all('li')
    name_category = breadcrumb_li[-2].find('a').string


def get_data_book(data, url):
    price_regex = r"\d+\.\d{2}"
    description = "Pas de description sur ce produit"

    if data.find(id="product_description"):
        description = data.find(id="product_description").find_next_sibling().string

    book = {
        "product_page_url": url,
        "universal_ product_code": data.find_all('td')[0].string,
        "title": data.h1.string,
        "price_including_tax": float(search(price_regex, data.find_all('td')[3].string).group()),
        "price_excluding_tax": float(search(price_regex, data.find_all('td')[2].string).group()),
        "number_available": data.find_all('td')[5].string,
        "product_description": description,
        "category": category_product(data),
        "review_rating": get_number_star(data.find(class_="star-rating")),
        "image_url": get_url_img(data),
    }
    return book
