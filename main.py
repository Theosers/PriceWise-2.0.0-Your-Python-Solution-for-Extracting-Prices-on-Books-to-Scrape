import requests
from bs4 import BeautifulSoup
import csv
import module
import fonction
import re


url_categorie = 'http://books.toscrape.com/'

categories = fonction.All_categories(url_categorie)

url_page = fonction.category_pages_url(url_categorie, categories) #récupère tout les urls de toute les pages d'une catégorie

fonction.get_full_category_bookslink(url_page) #récupère tout les liens des livres de toute les pages d'une catégorie

fonction.get_infos_book(links) # récupère les informations de tout les livres





