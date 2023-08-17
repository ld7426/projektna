from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv

website = "https://www.arso.gov.si/vode/podatki/amp/Ht_30.html" #spletna stran iz katere potegnemo prve podatke
result = requests.get(website)

content = result.text

soup = bs(content, "lxml") #rad imam juho al nekaj

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
    zacasna=vrstica.split("&#10")[0][1:]
    id = vrstica[-18:-3]
    #slovar[id] = zacasna.split(" - ")

    slovar.append({"Ime": zacasna.split(" - ")[0].replace("&#x010D;", "č").replace("&#x010C;", "Č").replace("&#x0160;", "Š").replace("&#x0161;", "š").replace("&#x017E;", "ž").replace("&#x017D;", "Ž"), "Reka":zacasna.split(" - ")[1].replace("&#x010D;", "č").replace("&#x010C;", "Č").replace("&#x0160;", "Š").replace("&#x0161;", "š").replace("&#x017E;", "ž").replace("&#x017D;", "Ž"), "ID":id})

print(slovar) #dobljen slovar povezuje imena postaj in identifikatorje

#zdaj lahko začnemo z downloadanjem podatkov posameznih postaj
polja = ["Ime", "Reka", "ID"]
with open("slovar.csv", "w", newline="") as csvfile:
    # Create a CSV writer using the field/column names
    writer = csv.DictWriter(csvfile, fieldnames=polja)
    
    # Write the header row (column names)
    writer.writeheader()
    
    # Write the data
    for row in slovar:
        writer.writerow(row)