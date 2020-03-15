import requests
import urllib.request
import os
from PIL import Image
import shutil
from bs4 import BeautifulSoup

LeSite = "https://www.lirescan.me"

os.chdir("C://Users//maroc//Desktop//Nouveau.dossier")

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens=lirescan(url)
    return [soup,ListeLiens]


def image(soup):
    ListeLiens = []
    while ListeLiens == []:
        Im = soup.findAll('img')[0]
        ListeLiens.append(Im["src"])
    return ListeLiens


def Next(url):
    uuu=isole1(url)
    bbb=isole(url)
    NextUrl=uuu+str(bbb+1)+'/'
    if lirescan(url)==lirescan(NextUrl):
        NextUrl="Fin du Manga"
    else:
        print(NextUrl)
    return NextUrl

def isole(url):
    bac=url.split('/')[-2]
    return int(bac)


def isole1(url):
    url2 = url.split(str(isole(url)))[0]
    return url2

def soupe(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def lirescan(url):
    ListeLiens = []
    img=""
    i=1
    while img == "":
        var = url + str(i)
        a = str(soupe(var).findAll("title"))
        if a == "[]":
            img = 'Fin du chapitre'
        i = i + 1
        ListeLiens.append(var)
    ListeLiens.pop(-1)
    LLL = []
    for elt in ListeLiens:
        soup = soupe(str(elt))
        babar = image(soup)
        kuji = "".join(map(str,babar))
        LLL.append(LeSite+kuji)
    return LLL