from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv


slovar=[*csv.DictReader(open('slovar.csv'))] #odprem in shranim slovar od prej kot slovar tukaj
#print(slovar)

page = "https://www.arso.gov.si/vode/podatki/amp/" #stran iz katere nalagam podatke

for vrstica in slovar:
    website= page + vrstica["ID"]
    stran = bs(requests.get(website).text, "lxml")
    table1 = stran.find("table", id="glavna")

    vrstepodatkov = []
    for i in table1.find_all("th"):
        title = i.text
        vrstepodatkov.append(title)

    #print(vrstepodatkov)
    pandatabelca = pd.DataFrame(columns = vrstepodatkov)

    for j in table1.find_all("tr")[1:]:
        try:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            length = len(pandatabelca)
            if row !=[]:
                pandatabelca.loc[length] = row
        except:
            raise Exception("Napaka pri iskanju vrstic")
    

    # spravimo v .csv file
    pandatabelca.to_csv("postaje/" + vrstica["ID"] + ".csv", index=False) #ime je enako IDju postaje, mogoče bi edino zbrisal .html stran?
    # pogledamo, da se da prebrati fajl
    try:
        poskusi = pd.read_csv("postaje/" + vrstica["ID"] + ".csv")
    except:
        raise Exception("Ustvarjene datoteke ni mogoče prebrati, preveri, če je ustvarjenje uspelo")
    
