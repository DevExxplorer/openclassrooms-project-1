from step_1 import scrap_book

def scrap_category(category_url):
    books_in_category # = Get le bon url, récupérer tous les livres de la categorie
    books = []
    for book in books_in_category:
        book = scrap_book(book)
        books.append(book)
    save_category(books)

def save_category(books):
    pass