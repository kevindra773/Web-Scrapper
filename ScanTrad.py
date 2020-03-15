import requests
import urllib.request
import os
from PIL import Image
import shutil
import urllib.parse
from bs4 import BeautifulSoup

LeSite = "https://scantrad.net/"

os.chdir("C://Users//maroc//Desktop//Nouveau.dossier")

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens=image(soup)
    return [soup,ListeLiens]


def image(soup):
    Img = soup.findAll('img')
    ListeLiens = []
    for item in Img:
        if 'id' in item.attrs and 'scimg'in item['id']:
            if item['data-src'] != "https://scantrad.net/images/scantrad.jpg":
                a= item['data-src']
                b= ListeLiens.append(LeSite+a)
    return ListeLiens


def Next(soup,url):
    uuu=isole1(url)
    bbb=isole(url)
    NextUrl=uuu+str(bbb+1)
    a=str(NextUrl)
    if image(soup)==[]:
        NextUrl = "Fin du Manga"
    return NextUrl

def isole(url):
    bac=url.split('/')[-1]
    return int(bac)


def isole1(url):
    url2 = url.split(str(isole(url)))[0]
    return url2
