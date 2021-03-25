import requests
from bs4 import BeautifulSoup
import csv

class livre:

    def __init__(self, soup, url):
        self.product_page_url = url
        self.universal_product_code = soup.findAll('td')[0].string
        self.title = soup.findAll('h1')[0].string
        self.price_including_tax = soup.findAll('td')[3].string
        self.prince_excluding_tax = soup.findAll('td')[2].string
        self.number_available = soup.findAll('td')[5].string
        self.product_description = soup.findAll('p')[3].string
        self.category = soup.findAll('a')[3].string
        self.review_rating = soup.findAll('td')[6].string
        self.image_url = soup.findAll('img')[0]['src']
        #        self.image_url = 'books.toscrape.com/' + image_url.replace('../../', '')

        self.infos = [self.product_page_url, self.universal_product_code, self.title, self.price_including_tax,
                      self.prince_excluding_tax,
                      self.number_available, self.product_description, self.category, self.review_rating,
                      self.image_url]

    def save_CSV(self):
        with open('eggs.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(
                ['product_page_url'] + ['universal_product_code'] + ['title'] + ['price_including_tax'] + [
                    'prince_excluding_tax'] +
                ['number_available'] + ['product_description'] + ['category'] + ['review_rating'] + ['image_url'])

            spamwriter.writerow([self.infos])

