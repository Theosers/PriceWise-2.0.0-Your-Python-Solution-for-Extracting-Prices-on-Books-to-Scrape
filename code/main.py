from Traitement import *
from save import *
from extract import *

url = 'http://books.toscrape.com/index.html'
extraire_PagePrincipal = extract(url)
extraire_PagePrincipal.get_soup()

Traiter_PagePrincipal = Traitement(extraire_PagePrincipal.soup)


for counter, category in enumerate(Traiter_PagePrincipal.traitement_soup_PagePrincipal()):

    extraire_category = extract(category)
    extraire_category.get_soup()
    Traiter_category = Traitement(extraire_category.soup)


    for page in range(1, int(Traiter_category.number_of_page()) + 1 ):

        if page == 1 :
            extraire_page = extract(extraire_category.url+ 'index' + '.html')
        else :
            extraire_page = extract(extraire_category.url+ 'page-' + str(page) + '.html')


        extraire_page.get_soup()
        Traiter_category = Traitement(extraire_page.soup)


        for counter,book in enumerate(Traiter_category.traitement_soup_category()):

            extraire_livre = extract(book)
            extraire_livre.get_soup()

            Traiter_livre = Traitement(extraire_livre.soup)

            save(Traiter_livre.traitement_soup_livres(book))