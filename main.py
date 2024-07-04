import get_book
import get_books_category
import get_all_books


def main():
    step = input(
        'Quelles données souhaitez-vous extraire : '
        'A) Un seul produit'
        'B) Tous les produits d\'une catégorie '
        'C) Tous les produits de toutes les catégories. '
        '[A/B/C]? : ')

    if step == 'A':
        get_book.save_book()
    elif step == 'B':
        get_books_category.save_books('mystery_3')
    elif step == 'C':
        get_all_books.save_all_books()
    else:
        print('Erreur : veuillez relancer le programme')


if __name__ == '__main__':
    main()
