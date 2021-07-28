import re


class Process:
    """
    Processes data from a web page in html form to extract relevant information.
    Args:
        soup(bs4.BeautifulSoup)
    """

    def __init__(self, soup):

        self.soup = soup

    def books_soup_process(self, url):
        """

        :param url: url from the web page of a book
        :return: relevant information about the book (list)
        """
        product_page_url = url
        universal_product_code = self.soup.find('td').string
        title = self.soup.find('h1').string
        price_including_tax = self.soup.findAll('td')[3].string
        prince_excluding_tax = self.soup.findAll('td')[2].string
        number_available = self.soup.findAll('td')[5].string
        product_description = self.soup.findAll('p')[3].string
        category = self.soup.findAll('a')[3].string
        review_rating = self.soup.findAll('td')[6].string
        image_url = self.soup.find('img')['src']
        image_url = image_url.replace('../../', 'http://books.toscrape.com/')

        infos = [product_page_url, universal_product_code, title, price_including_tax, prince_excluding_tax,
                 number_available, product_description, category, review_rating, image_url]
        return infos

    def number_of_page(self):
        """

        :return: the number of book pages that exist in a book category (int)
        """
        number_of_page = re.sub('[1\D]', '', str(self.soup.findAll('li')[-2].string))

        if number_of_page == '':
            number_of_page = 1

        return int(number_of_page)

    def soup_category_process(self):
        """
        retrieves all book links from a page in a book category
        :return: books links (list)
        """
        articles = self.soup.findAll('article')
        Books_links = []

        for article in articles:
            a = article.find('a')
            link = a['href']
            link = link.replace('../../../', '')

            Books_links.append('http://books.toscrape.com/catalogue/' + link)

        return Books_links

    def soup_PagePrincipal_process(self):
        """

        :return: categories listed on the main page (list)
        """
        categories = []
        ul = self.soup.findAll('ul')[1]
        a = ul.findAll('a')
        a.pop(0)

        for counter, category in enumerate(a):
            link = a[counter]['href']
            link = link.replace('../', '')
            link = link.replace('index.html', '')
            link = 'http://books.toscrape.com/' + link
            categories.append((link))

        return categories
