# BS 1.2.0 (Books Scraper)

## Table of Contents

1. General Info
2. How to use this repository

### General Info

***

This is the beta version of the price extraction program BS 2.0.0, developed in Python.
The goal is to extract all kind of informations on the website Books to Scrape (http://books.toscrape.com/). 

The informations are ( store in the file product.csv) :

- Url
- Universal product code (upc)
- Title
- Price including taxes
- Price excluding taxes
- Number of books available
- Description
- Catégory
- Note of the reviews
- Url of the picture


Then download and save the image file of each product.

## How to use this repository

***

This program will require python 3.9.6 installed : https://www.python.org/downloads/

In a new virtual environment, install all dependency :
```
pip install -r requirements.txt
```
To execute BS :

launch the launcher.sh 

```
sh launcher.sh
```
