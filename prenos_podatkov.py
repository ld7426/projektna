from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

website = "https://www.arso.gov.si/vode/podatki/amp/Ht_30.html" #spletna stran iz katere potegnemo prve podatke
result = requests.get(website)

content = result.text

soup = bs(content, "lxml") #rad imam juho al nekaj

#print(content)

slovar = dict({})

deljensoup = content.split(">") #razdelim na vrstice
uporabnevrstice = []

for vrstica in deljensoup:
    if 'area' in str(vrstica):
        uporabnevrstice.append(vrstica) #dam stran neuporabne vrstice



for indeks, vrstica in enumerate(uporabnevrstice):
    uporabnevrstice[indeks] = str(vrstica).split('alt=')[1] #žeim extractat ime, vrstica s torej začne z imenom, ki pa ima še " spredaj, skoraj ziher je to daleč od optimalnega :D

for vrstica in uporabnevrstice:
    zacasna=vrstica.split("&#10")[0][1:]
    id = vrstica[-18:-3]
    slovar[id] = zacasna.split(" - ")

print(slovar) #dobljen slovar povezuje imena postaj in identifikatorje

#zdaj lahko začnemo z downloadanjem podatkov posameznih postaj

