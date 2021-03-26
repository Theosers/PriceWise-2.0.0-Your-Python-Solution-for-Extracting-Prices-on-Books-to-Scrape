import requests
from bs4 import BeautifulSoup
import csv
import module
import re

def get_infos_book(links):

    books = []

    for n in range(len(links)):

        url = links[n]
        reponse = requests.get(url)
        if reponse.ok:
            soup = BeautifulSoup(reponse.text, 'html.parser')
            books.append(module.livre(soup, url))

    for book in books:
        module.livre.save_CSV(book)


def category_pages_url(url_categorie, categories) :
    url_page = []
    for link_categorie in categories :

        reponse = requests.get(url_categorie + link_categorie[1])

        if reponse.ok:

            soup = BeautifulSoup(reponse.text, 'html.parser')
            number_of_page = re.sub('[1\D]', '', str(soup.findAll('li')[-2].string))

            if number_of_page == '':
                number_of_page = 1

            for page in range(1, int(number_of_page) +1):
                if page == 1 :
                    url_page.append( url_categorie + link_categorie[1].replace('index.html', '') + 'index' + '.html' )
                else:
                    url_page.append( url_categorie + link_categorie[1].replace('index.html','') + 'page-' + str(page) + '.html' )
        else:
            print("Vous n'avez pas accès à cette url")

    return url_page


def get_full_category_bookslink(url_page):

    for counter, page in enumerate(url_page) :

        reponse = requests.get(url_page[counter])
        if reponse.ok:

            links = []

            soup = BeautifulSoup(reponse.text, 'html.parser')
            articles = soup.findAll('article')

            for article in articles:
                a = article.find('a')
                link = a['href']
                link = link.replace('../../../', '')
                links.append('http://books.toscrape.com/catalogue/' + link)
        else:
            print("Vous n'avez pas accès à cette page")

    return links

def All_categories(url_categorie) :
    categories = []

    reponse = requests.get(url_categorie)
    if reponse.ok:

        soup = BeautifulSoup(reponse.text, 'html.parser')
        ul = soup.findAll('ul')[1]
        a = ul.findAll('a')
        a.pop(0)

        for counter, categorie   in enumerate(a) :
            name = re.sub('[\s]', '', str(categorie.string))
            link = a[counter]['href']
            link = link.replace('../', '')
            categories.append((name, link))     #On obtient un tuple contenant le nom de la catégorie et son lien relatif

        return categories
    else :
        print("Vous n'avez pas accès à cette url")

