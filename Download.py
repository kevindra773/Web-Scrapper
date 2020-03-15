import requests
import urllib.request
import os
from PIL import Image
import shutil
if __name__ == '__main__':
    def dossier():
        os.chdir(r"C:\Users\maroc\Desktop\GitHub\Web-Scrapper")

    dossier()
import MangaFoxScrapper as MF
import MangaLeno as ML
import MangaReaderScrapper as MR
import MangaZuki as MZ
import ScanFr as SF
import LelScan as LS
import ScanVF as SV
import Scanop as SO
import LireScan as LSN
import ScanTrad as ST
path = r"C:\Users\maroc"

def Download(download_url,name):
    if download_url != "Fin du Manga":
        if download_url != "https://s3.mangareader.net/images/erogesopt.jpg":
            #On fait une requête et on cache le fait que l'on est un robot
            req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})

            #on prend le content de la page en bytes
            web_byte = urllib.request.urlopen(req).read()

            #on écrit le content dans un fichier test et on lui file le bon format
            open(name + '.jpg','wb').write(web_byte)
            print(download_url)


def Compression():
    os.mkdir("Compr")
    ListeNon = []
    for elt in os.listdir():
        try:
            print(elt)
            im = Image.open(elt)
            im.save("Compr/" + elt,quality = 50, optimize = True)
        except:
            try:
                shutil.copy(elt,"Compr/" + elt)
            except:
                print("Erreur pour elt")
                ListeNon.append(elt)
    return ListeNon



class Site:
    def __init__(self,url,Titre):
        self.url = url
        self.soup = ""
        self.ListeLiens = []
        self.Titre = Titre
        self.chapter = ""
        self.compteur = 0


    def Initialisation(self):
        os.chdir(path)
        if self.Titre not in os.listdir():
            os.mkdir(self.Titre)
        os.chdir(self.Titre)
        with open('Titre.txt','w+') as file:
            file.write(self.Titre)


    def Navigate(self):
        if 'mangafox' in self.url:
            [self.soup,self.ListeLiens] = MF.Navigate(self.url)
        if 'manganelo' in self.url or 'mangakakalot' in self.url:
            [self.soup,self.ListeLiens] = ML.Navigate(self.url)
        if 'mangareader' in self.url:
            [self.soup,self.ListeLiens] = MR.Navigate(self.url)
        if 'mangazuki' in self.url:
            [self.soup,self.ListeLiens] = MZ.Navigate(self.url)
        if 'scan-fr' in self.url:
            [self.soup,self.ListeLiens] = SF.Navigate(self.url)
        if 'https://www.lelscan-vf.com/' in self.url:
            [self.soup,self.ListeLiens] = LS.Navigate(self.url)
        if 'https://www.scan-vf.net/' in self.url:
            [self.soup,self.ListeLiens] = SV.Navigate(self.url)
        if 'scan-op' in self.url:
            [self.soup,self.ListeLiens] = SO.Navigate(self.url)
        if 'https://www.lirescan.me/' in self.url:
            [self.soup,self.ListeLiens] = LSN.Navigate(self.url)
        if 'scantrad' in self.url:
            [self.soup,self.ListeLiens] = ST.Navigate(self.url)
    def Next(self):
        if 'mangafox' in self.url:
            self.url = MF.Next(self.soup)
        if 'manganelo' in self.url or 'mangakakalot' in self.url:
            self.url = ML.Next(self.soup)
        if 'mangareader' in self.url:
            self.url = MR.Next(self.soup)
        if 'mangazuki' in self.url:
            self.url = MZ.Next(self.soup)
        if 'svan-vf' in self.url:
            self.url = SV.chapitre(self.url,self.chap)
        if 'scan-fr'in self.url:
            self.url= SF.Next(self.soup,self.url)
        if 'https://www.lelscan-vf.com/' in self.url:
            self.url= LS.Next(self.soup,self.url)
        if 'https://www.scan-vf.net/' in self.url:
            self.url= SV.Next(self.soup,self.url)
        if 'scan-op' in self.url:
            self.url = SO.Next(self.soup,self.url)
        if 'https://www.lirescan.me/' in self.url:
            self.url = LSN.Next(self.url)
        if 'scantrad' in self.url:
            self.url = ST.Next(self.soup,self.url)
    def Chapter(self):
        if 'mangafox' in self.url:
            n = self.url.find('/chapter')
            m = self.url[n+1:].find('-')
            self.chapter = self.url[n+1:n+m+3]
        if 'manganelo' in self.url or 'mangakakalot' in self.url:
            n = self.url.find("/chapter")
            m = self.url[n+1:].find('/c')
            self.chapter = url[n+m+2:]
        if 'mangareader' in self.url:
            n= self.url.find('reader')
            m=url[n:].find('/')
            l = url[n+m+1:].find('/')
            k = url[n+m+1+l+1:].find('/')
            nom = self.url[n+m+1:m+n+k+l+2]
            nom.replace('/','_')
            self.url = nom
        if 'mangazuki' in self.url:
            n = self.url.find("chapter")
            self.chapter = self.url[n:-1]

    def DownloadListe(self):
        for lien in self.ListeLiens:
            self.compteur +=1
            Download(lien,f"{self.compteur:05d}")

    def InitSoup(self):
        while self.url != "Fin du Manga":
            self.Navigate()
            self.Initialisation()
            self.DownloadListe()
            self.Next()
            print(self.url)
    def ReprendreSoup(self):
        os.chdir(self.Titre)
        self.Navigate()
        self.Next()
        while self.url != "Fin du Manga":
            self.Navigate()
            self.DownloadListe()
            self.Next()
        os.chdir("..")



def Reprise():
    os.chdir(path)
    ListeSite = []
    for dossier in os.listdir():
        if os.path.isdir(dossier):
            os.chdir(dossier)
            with open("LastUrl.txt","r") as file:
                url = file.read()
            with open("Titre.txt","r") as file:
                Titre = file.read()
            Sitee = Site(url,Titre)
            ListeSite.append(Sitee)
            os.chdir("..")
    for site in ListeSite:
        site.ReprendreSoup()
    return ListeSite

def BoucleCompr():
    os.chdir(path)
    for dossier in os.listdir():
        if os.path.isdir(dossier):
            os.chdir(dossier)
            Compression()
            os.chdir("..")
