import requests
from bs4 import BeautifulSoup
import csv
import module
import fonction
import re


extraire_PagePrincipal = module.extract('http://books.toscrape.com/index.html')
extraire_PagePrincipal.get_soup()

Traiter_PagePrincipal = module.Traitement(extraire_PagePrincipal.soup)


for counter, category in enumerate(Traiter_PagePrincipal.traitement_soup_PagePrincipal()):

    extraire_category = module.extract(category)
    extraire_category.get_soup()
    Traiter_category = module.Traitement(extraire_category.soup)


    for page in range(1, int(Traiter_category.number_of_page()) +1 ):

        if page == 1 :
            extraire_page = module.extract(extraire_category.url+ 'index' + '.html')
        else :
            extraire_page = module.extract(extraire_category.url+ 'page-' + str(page) + '.html')


        extraire_page.get_soup()
        Traiter_category = module.Traitement(extraire_page.soup)


        for counter,book in enumerate(Traiter_category.traitement_soup_category()):

            extraire_livre = module.extract(book)
            extraire_livre.get_soup()

            Traiter_livre = module.Traitement(extraire_livre.soup)

            module.save(Traiter_livre.traitement_soup_livres(book))
