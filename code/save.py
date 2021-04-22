import csv
import os
from extract import *


class save:

    def __init__(self, infos):

        self.infos = infos

        if not os.path.exists('data'):
            os.makedirs('data')

        with open('data/produits.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            if os.path.getsize("data/produits.csv") == 0:
                spamwriter.writerow(
                    ['product_page_url'] + ['universal_product_code'] + ['title'] + ['price_including_tax'] + [
                        'prince_excluding_tax'] +
                    ['number_available'] + ['product_description'] + ['category'] + ['review_rating'] + ['image_url'])

            spamwriter.writerow([self.infos])

        with open('data//' + infos[2].translate({ord(i): None for i in '<>:"“\|?/*'}) + ".jpg", "wb") as f:
            a = extract(infos[9])
            f.write(a.get_url_to_download())
