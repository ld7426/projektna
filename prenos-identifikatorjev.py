from bs4 import BeautifulSoup as bs
import requests
#import pandas as pd
import csv

website = "https://www.arso.gov.si/vode/podatki/amp/Ht_30.html" #spletna stran iz katere potegnemo prve podatke
result = requests.get(website)

content = result.text

soup = bs(content, "lxml") #rad imam juho al nekaj, modul se imenuje juha

#print(content)

slovar = []

deljensoup = content.split(">") #razdelim na vrstice
uporabnevrstice = []

for vrstica in deljensoup:
    if 'area' in str(vrstica):
        uporabnevrstice.append(vrstica) #dam stran neuporabne vrstice



for indeks, vrstica in enumerate(uporabnevrstice):
    uporabnevrstice[indeks] = str(vrstica).split('alt=')[1] #žeim extractat ime, vrstica s torej začne z imenom, ki pa ima še " spredaj, skoraj ziher je to daleč od optimalnega :D

for vrstica in uporabnevrstice:
    zacasna=vrstica.split("&#10")[0][1:] #ta znak je bil na koncu vsakega podatka zato splittam po njem
    zacasna = zacasna.replace("&#x010D;", "č").replace("&#x010C;", "Č").replace("&#x0160;", "Š").replace("&#x0161;", "š").replace("&#x017E;", "ž").replace("&#x017D;", "Ž") 
    #tale koda je ugly af, ampak deluje, tak da se ne bom ukvarjal z drugim, zamenja pa čudne characterje s šumniki, ker so čudni characterji motili, na primer imeli so ; notr
    zacasna = zacasna.split(" - ")
    id = vrstica[-18:-13]
    
    slovar.append({"Ime": zacasna[0], "Reka":zacasna[-1], "ID":id})
    

#print(slovar) #dobljen slovar povezuje imena postaj, reko in identifikatorje

#zdaj lahko začnemo z downloadanjem podatkov posameznih postaj
polja = ["Ime", "Reka", "ID"]
with open("slovar.csv", "w", newline="") as csvfile:
    # Create a CSV writer using the field/column names
    writer = csv.DictWriter(csvfile, fieldnames=polja)
    
    # Napišemo uvodno 
    writer.writeheader()
    
    # Write the data
    for row in slovar:
        writer.writerow(row)

