# This program was done by Alexander Mitchell
# It is meant to get the background info on Steve Fox

from bs4 import BeautifulSoup
import requests
from lxml import etree

r = requests.get("https://tekken.fandom.com/wiki/Steve_Fox")

if r.status_code == 400 or r.status_code == 50:
    print("Connection bad: Houston we have a problem \n")
elif r.status_code == 200:
    print("Connection good: We're good!! \n")

soup = BeautifulSoup(r.content,'lxml')

print("\nHere is some info about the best Character in Tekken: \n")

# Print Steve fox's info
ps = soup.find_all('p')

for el in ps[0:4]:
    print(el.text)

