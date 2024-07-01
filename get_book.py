import books_functions


def init_get_book(slug_book):
    if slug_book != '':
        home = 'https://books.toscrape.com/catalogue/' + slug_book + '/index.html'
    else:
        home = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

    data_book = books_functions.get_info_book(books_functions.parse_html(home))
    books_functions.create_csv(data_book)

