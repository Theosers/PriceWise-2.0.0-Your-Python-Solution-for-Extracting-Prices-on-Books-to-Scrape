import requests
from bs4 import BeautifulSoup

class extract :

    def __init__(self, url):
        self.url = url
        self.soup = None

    def get_soup(self):

        reponse = requests.get(self.url)
        if reponse.ok:
            soup = BeautifulSoup(reponse.content, 'html.parser')

        else:
            print("non")
        self.soup = soup


