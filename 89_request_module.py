import requests
from bs4 import BeautifulSoup

#response = requests.get("https://www.google.com")
r = requests.get("https://www.google.com")

#print(response.text) # will print html source code
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())


for anchor in soup.find_all("a"):
    print(anchor.text)

