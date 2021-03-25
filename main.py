import requests
from bs4 import BeautifulSoup
import csv
import module

links = []
livres = []

url_page = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'

reponse = requests.get(url_page)
if reponse.ok:
    soup = BeautifulSoup(reponse.text, 'html.parser')
    articles = soup.findAll('article')

    for article in articles:
        a = article.find('a')
        link = a['href']
        link = link.replace('../../../', '')
        links.append('http://books.toscrape.com/catalogue/' + link)
else:
    print("Vous n'avez pas accès à cette page")






for n in range(len(links)):

    url = links[n]

    reponse = requests.get(url)
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')


        livres.append(module.livre(soup, url))

for a in livres:
    print(a.infos)

        #livre1.save_CSV()


