from process import Process
from save import Save
from extract import Extract

if __name__ == "__main__":

    url = 'http://books.toscrape.com/index.html'

    extractMainPage = Extract(url)
    extractMainPage.get_soup()
    mainPageProcess = Process(extractMainPage.soup)

    for counter, category in enumerate(mainPageProcess.soup_PagePrincipal_process()):

        list_of_book = []
        category_extract = Extract(category)
        category_extract.get_soup()
        category_process = Process(category_extract.soup)

        for page in range(1, category_process.number_of_page() + 1):

            if page == 1:
                page_extract = Extract(f"{category_extract.url}index.html")
            else:
                page_extract = Extract(f"{category_extract.url}page-{str(page)}.html")

            page_extract.get_soup()
            category_process = Process(page_extract.soup)

            for counter2, book in enumerate(category_process.soup_category_process()):
                book_extract = Extract(book)
                book_extract.get_soup()

                book_process = Process(book_extract.soup)
                Save(book_process.books_soup_process(book), book_process.books_soup_process(book)[7])

                print(f"{counter} categories on {len(mainPageProcess.soup_PagePrincipal_process())} extracted")
                print(f"----------------------------------------------")
                print(f"{int(counter / len(mainPageProcess.soup_PagePrincipal_process()) * 100)}% data extracted")
                print(f"----------------------------------------------\n")
