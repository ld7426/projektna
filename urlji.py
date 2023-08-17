import requests
from bs4 import BeautifulSoup

reqs = requests.get("https://www.arso.gov.si/vode/podatki/amp/Ht_30.html")
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))