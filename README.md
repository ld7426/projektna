# Analiza slovenskih vodotokov iz podatkov dostopnih na ARSO

Pri predmetu Uvod v programiranje sem moral pripraviti analizo podatkov v Pythonu z uporabo Jupyter Notebooka.

Najprej sem iz spletne strani ARSO Vode pobral pobral polurne podatke 180 samodejnih merilnih postaj za zadnjih 30 dni in jih shranil v csv datoteke. Hkrati pa sem tudi ustvaril slovar, ki povezuje imena postaj in podatek na kateri reki postaja leži, ter identifikacijsko številko od postaje, kot jo uporablja ARSO.

Podatke sem nato na razne načine obdelal v Jupyter Notebooku s pandami in matplotlibom.

## Navodila za uporabo

Programa *podatki-posameznih-postaj.py* in *prenos-identifikatorjev.py* prvo iz spleta pobereta podatke. Oba programa se lahko zažene tudi iz zvezka *Analiza.ipynb*. Pomembno je, da se prvo zažene *prenos-identifikatorjev.py* (in da imamo dostop do interneta), saj *podatki-posameznih-postaj.py* potrebuje datoteko *slovar.csv*, ki nastane pri tem. Pri programu *podatki-posameznih-postaj.py* je potrebno nekaj potrpežljivosti, saj nalaganje traja par minut.

Za zagon ni potrebnega nobenega dodatnega vnosa, vse je že pripravljeno na uporabo.

Ko se podatki prenesejo se lahko začne uporabljati še zvezek *Analiza.ipynb*. Delovanje je dokaj preprosto, predlagam, da se prvo sproži ukaz **Run all cells** in se nato še lastnoročno sprehodimo po zvezku. Zvezek vsebuje nekatere interaktivne vsebine, ki delujejo samo, ko je njihova celica zadnja pognana.

V osnovi se v zvezku analizira naključna postaja, a uporabnik si lahko sam izbere, katero postajo hoče, da namesto naključne vpiše svojo lastno izbiro.


## Problemi z matplotlib

Če se graf ne pokaže je potrebno pognati ukaza  
 *plt.close()*  
*%matplotlib inline*  
in šele nato še enkrat zagnati celico, ki naj bi prikazala graf.




vir: [ARSO](http://www.arso.gov.si/vode/podatki/)
