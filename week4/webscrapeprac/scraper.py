from bs4 import BeautifulSoup
import requests
# from html.parser import HTMLParser
from lxml import etree

# Gets google
r = requests.get('http://google.com')

soup = BeautifulSoup(r.content,'lxml') 

# returns text content of divs on google.com
divs = soup.div.text
print(divs)

# returns text content of footer on google.com
footer = soup.find(id="footer")
print(footer.text)

# Returns what is in the p element
pel = soup.p.text
print(pel)