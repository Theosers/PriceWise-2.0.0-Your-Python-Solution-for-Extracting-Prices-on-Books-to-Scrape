import requests
from bs4 import BeautifulSoup


class Extract:
    """
    Each of the methods of this class retrieves data from a Web page.
    Args:
        url(str): url of a web page
        soup(None): The data associated to this url in html form (after using get_soup module)
    """

    def __init__(self, url):
        self.url = url
        self.soup = None

    def get_soup(self):
        """
        Get the code of a web page and save it as html
        """
        response = requests.get(self.url)
        if response.ok:
            self.soup = BeautifulSoup(response.content, 'html.parser')

        else:
            with open('log.txt', 'w', encoding='utf-8') as error:
                error.write('Sorry, we did not have access to the url :' + self.url)

    def get_url_to_download(self):
        """
        takes as input the irl of an image
        :return: the content of the web page (the data of an image)
        """
        response = requests.get(self.url, stream=True)
        return response.content
