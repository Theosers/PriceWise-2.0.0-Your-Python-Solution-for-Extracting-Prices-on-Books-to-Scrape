import requests
from bs4 import BeautifulSoup
import csv
import os
import re


class extract :

    def __init__(self, url):
        self.url = url
        self.soup = None

    def get_soup(self):

        reponse = requests.get(self.url)
        if reponse.ok:
            soup = BeautifulSoup(reponse.text, 'html.parser')

        else:
            print("non")
        self.soup = soup



class Traitement :

    def __init__(self, soup):

        self.soup = soup


    def traitement_soup_livres(self, url):

        product_page_url = url
        universal_product_code = self.soup.findAll('td')[0].string
        title = self.soup.findAll('h1')[0].string
        price_including_tax = self.soup.findAll('td')[3].string
        prince_excluding_tax = self.soup.findAll('td')[2].string
        number_available = self.soup.findAll('td')[5].string
        product_description = self.soup.findAll('p')[3].string
        category = self.soup.findAll('a')[3].string
        review_rating = self.soup.findAll('td')[6].string
        image_url = self.soup.findAll('img')[0]['src']

        infos = [product_page_url, universal_product_code, title, price_including_tax,
                 prince_excluding_tax,
                 number_available, product_description, category, review_rating,
                 image_url]
        return infos

    def number_of_page(self):

        number_of_page = re.sub('[1\D]', '', str(self.soup.findAll('li')[-2].string))
        if number_of_page == '':
            number_of_page = 1

        print(number_of_page)
        return number_of_page


    def traitement_soup_category(self):


        articles = self.soup.findAll('article')
        Books_links = []

        for article in articles:
            a = article.find('a')
            link = a['href']
            link = link.replace('../../../', '')

            Books_links.append('http://books.toscrape.com/catalogue/' + link)

        return Books_links


    def traitement_soup_PagePrincipal(self):
        categories = []
        ul = self.soup.findAll('ul')[1]
        a = ul.findAll('a')
        a.pop(0)

        for counter, categorie in enumerate(a):
            #name = re.sub('[\s]', '', str(categorie.string))
            link = a[counter]['href']
            link = link.replace('../', '')
            link = link.replace('index.html', '')
            link = 'http://books.toscrape.com/' + link
            categories.append((link))  # On obtient un tuple contenant le nom de la catégorie et son lien relatif

        return categories

class save :

    def __init__(self, infos):

        self.infos = infos

        with open('eggs.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            if os.path.getsize("eggs.csv") == 0:
                spamwriter.writerow(
                    ['product_page_url'] + ['universal_product_code'] + ['title'] + ['price_including_tax'] + [
                        'prince_excluding_tax'] +
                    ['number_available'] + ['product_description'] + ['category'] + ['review_rating'] + ['image_url'])

            spamwriter.writerow([self.infos])