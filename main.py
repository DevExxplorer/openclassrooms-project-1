from get_book import init_get_book
from get_all_books import init_get_all_books
from get_books_category import init_get_books_category


def main():
    step = input('Quelles données souhaitez-vous extraire : A) Un seul produit B) Tous les produits d\'une catégorie C) Tous les produits de toutes les catégories. [A/B/C]? : ')

    if step == 'A':
        slug_book = input('Vous pouvez choisir un livre en copiant son slug (par défault retourne le premier livre) : ')
        init_get_book(slug_book)
    elif step == 'B':
        init_get_books_category()
    elif step == 'C':
        init_get_all_books()
    else:
        print('Erreur : Aucun donnée séléctionnée')


if __name__ == '__main__':
    main()
