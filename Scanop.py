import requests
import urllib.request
import os
from PIL import Image
import shutil
import urllib.parse
from bs4 import BeautifulSoup

LeSite = "https://scan-op.com/"

os.chdir("C://Users//maroc//Desktop//Nouveau.dossier")

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens=image(soup)
    return [soup,ListeLiens]


def image(soup):
    ListeLiens = []
    Im = soup.findAll('img')
    for elt in Im:
        if 'class' in elt.attrs and elt['class']==["img-responsive"]:
            var = elt['data-src']
            proto, url = urllib.parse.splittype(var.strip())
            ListeLiens.append(proto + ":" + urllib.parse.quote(url))
    return ListeLiens


def Next(soup,url):
    uuu=isole1(url)
    bbb=isole(url)
    NextUrl=uuu+str(bbb+1)
    a=str(NextUrl)
    if image(soup) == []:
        NextUrl = "Fin du Manga"
        print(NextUrl)
    else:
        print(NextUrl)
    return NextUrl

def isole(url):
    bac=url.split('/')[-1]
    return int(bac)


def isole1(url):
    url2 = url.split(str(isole(url)))[0]
    return url2

"""
Explication:

import urllib.parse
urlpourri = ' http://funquizzes.fun/uploads/manga/vinland-saga/Manga Vinland Saga/170/001.png'
urlpaspourri = urlpourri.strip()
print(urlpaspourri)  # ohhh ya plus l'espace au début
proto,path = urllib.parse.splittype(urlpaspourri)
print(proto)
print(path)  # maintenant ya plus le ":"
path_avec_quote = urllib.parse.quote(path)
print(path_avec_quote)  # on quote la bonne partie
url_avec_quote = proto + ":" + path_avec_quote  # puis on recolle tout
print(url_avec_quote)"""