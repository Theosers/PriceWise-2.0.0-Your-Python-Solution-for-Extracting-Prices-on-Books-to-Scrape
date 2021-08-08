import csv
import os
from extract import Extract


class Save:
    """
    1.Retrieves and saves the following data in a csv file for each category of book:
    - product_page_url
    -universal_product_code
    -title
    -price_including_tax
    -prince_excluding_tax
    -number_available
    -product_description
    -category
    -review_rating
    -image_url

    2.Then the image of each book is extracted from the image url and saved in a jpg file
    """

    def __init__(self, infos, category):

        self.infos = infos
        self.category = category
        if not os.path.exists('data/category'):
            os.makedirs('data/category')

        with open('data/category/' + category + '.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            if os.path.getsize("data/category/" + category + '.csv') == 0:
                spamwriter.writerow(
                    ['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
                     'prince_excluding_tax',
                     'number_available', 'product_description', 'category', 'review_rating', 'image_url'])

            spamwriter.writerow([self.infos])

        if not os.path.exists('data/images/' + category):
            os.makedirs('data/images/' + category)

        with open('data/images/' + category + "/" + infos[2].translate({ord(i): None for i in '<>:"“\|?/*'}) + ".jpg",
                  "wb") as f:
            a = Extract(infos[9])
            f.write(a.get_url_to_download())
