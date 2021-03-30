import requests
from bs4 import BeautifulSoup


class extract:

    def __init__(self, url):
        self.url = url
        self.soup = None

    def get_soup(self):

        reponse = requests.get(self.url)
        if reponse.ok:
            soup = BeautifulSoup(reponse.content, 'html.parser')

        else:
            with open('log.txt', 'w', encoding='utf-8') as erreur:
                erreur.write('Désolé, nous n\'avons pas eu accès à l\'url :' + self.url)
        self.soup = soup

    def get_url_to_download(self):
        reponse = requests.get(self.url, stream=True)
        return reponse.content
