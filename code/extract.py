import requests
from bs4 import BeautifulSoup


class Extract:

    def __init__(self, url):
        self.url = url
        self.soup = None

    def get_soup(self):

        response = requests.get(self.url)
        if response.ok:
            soup = BeautifulSoup(response.content, 'html.parser')

        else:
            with open('log.txt', 'w', encoding='utf-8') as error:
                error.write('Désolé, nous n\'avons pas eu accès à l\'url :' + self.url)
        self.soup = soup

    def get_url_to_download(self):
        response = requests.get(self.url, stream=True)
        return response.content
