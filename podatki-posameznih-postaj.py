from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv

stej = 0
slovar=[*csv.DictReader(open('slovar.csv'))] #odprem in shranim slovar od prej kot slovar tukaj
#print(slovar)


page = "https://www.arso.gov.si/vode/podatki/amp/" #stran iz katere nalagam podatke

for vrstica in slovar:
    stej = stej+1
    website= page + vrstica["ID"] + "_t_30.html" #spletne stran, ki se spreminja glede na ID postaje
    stran = bs(requests.get(website).text, "lxml") #mogoče ne bi bilo treba uporabiti bs?
    table1 = stran.find("table", id="glavna")

    vrstepodatkov = []
    for i in table1.find_all("th"):
        title = i.text.replace("Â", "") #ne vem zakaj je ta znak notr, ampak ga je treba odstranit
        vrstepodatkov.append(title)

    #print(vrstepodatkov)
    pandatabelca = pd.DataFrame(columns = vrstepodatkov)

    for j in table1.find_all("tr")[1:]:
        try:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            length = len(pandatabelca)
            if row !=[]: # nekatere vrstice so bile prazne, zato sem jih izpustil, da ne povzročajo problemov
                pandatabelca.loc[length] = row
        except:
            raise Exception("Napaka pri iskanju vrstic")
    
    pandatabelca = pandatabelca[::-1] #obrnemo tabelo, da je časovno urejena
    
    # spravimo v .csv file
    pandatabelca.to_csv("postaje/" + vrstica["ID"] + ".csv", index=False) #ime je enako IDju postaje
    # pogledamo, da se da prebrati fajl
    try:
        poskusi = pd.read_csv("postaje/" + vrstica["ID"] + ".csv")

    except:
        raise Exception("Ustvarjene datoteke ni mogoče prebrati, preveri, če je ustvarjanje uspelo")
    
    print("Prenešeno " + str(stej) + " od " + str(len(slovar)) + " postaj.") #izpiše koliko postaj je že prenešenih, lahko se tudi zakomentira, če ne želiš izpisa