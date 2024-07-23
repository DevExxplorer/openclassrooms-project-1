from get_book import save_book
from get_books_category import save_books_category
from get_all_books import save_all_books


def main():
    step = input(
        'Quelles données souhaitez-vous extraire :\n'
        'A) Un seul produit\n'
        'B) Tous les produits d\'une catégorie\n'
        'C) Tous les produits de toutes les catégories.\n'
        '[A/B/C]? : ')

    if step == 'A':
        save_book()
    elif step == 'B':
        save_books_category('mystery_3')
    elif step == 'C':
        save_all_books()
    else:
        print('Erreur: veuillez contacter un administrateur')


if __name__ == '__main__':
    main()
