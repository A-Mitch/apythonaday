# This program was done by Alexander Mitchell
from bs4 import BeautifulSoup
import requests
from lxml import etree

# What did I do
# 1. Open John's website and go through it/make it a beautiful soup object
# 2. I found all of John's information with this method: print(soup.prettify())
# 3. From there I saw what I needed to target.
# 4. I targeted those Items and returned them as a string

with open('bio.html') as f:
    soup = BeautifulSoup(f, 'lxml')

inf = []

for info in soup.find_all(id='red'):
    inf.append(info.text)

print("Here is John's info: "+str(' | '.join(inf)))

# Just closes the file
f.close()
