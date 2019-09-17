from bs4 import BeautifulSoup
import requests
from lxml import etree

r = requests.get("https://nytimes.com")

if r.status_code == 400 or r.status_code == 500:
    print("Connection bad: Houston we have a problem \n")
elif r.status_code == 200:
    print("Connection good: We're good!! \n")

soup = BeautifulSoup(r.content, 'lxml')

print("\nHere are the current headlines \n")

# This gets the current headlines from New York Times
# span class="balancedHeadline"
# headlines = soup.find(span="balancedHeadline").at
