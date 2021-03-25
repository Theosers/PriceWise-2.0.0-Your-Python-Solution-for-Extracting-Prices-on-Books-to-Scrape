import requests
from bs4 import BeautifulSoup
import csv
import module

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
reponse = requests.get(url)
if reponse.ok:
    soup = BeautifulSoup(reponse.text, 'html.parser')

    livre1 = module.livre(soup,'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
    # print(livre1.infos)
    livre1.save_CSV()


