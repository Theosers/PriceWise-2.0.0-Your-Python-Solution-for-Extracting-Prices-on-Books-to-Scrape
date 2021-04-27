# BS 1.2.0 (Books Scraper)

## Table of Contents

1. General Info
2. Comment utiliser ce dépôt

### General Info

***

Ceci est la version béta du programme d'extraction de prix BS 2.0.0, développé en Python, dont le but est d'extraire les
informations tarifaires du site Books to Scrape (http://books.toscrape.com/). La première version de ce programme est
disponible ici (https://github.com/Theosers/P2)

Récupère à l'execution les données suivante pour chaque produit (stocker dans un fichier produits.csv) :

- Url
- Code produit universel (upc)
- Titre
- Prix incluant les taxes
- Prix expluant les taxes
- Nombre d'ouvrages disponibles
- Description
- Catégorie
- Note des avis
- Url de l'image

Puis télécharge et enregistre le fichier image de chaque produit.

## Comment utiliser ce dépôt

***
Dans un nouvel environnement virtuel, installer toutes les dépendances :
```
pip install -r requirements.txt
```
Exécuter BS :

Aller dans le dossier P2-POO puis lancer le launcher.sh 

```
sh launcher.sh
```
