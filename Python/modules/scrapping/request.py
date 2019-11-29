from requests import get
from bs4 import BeautifulSoup
url = "http://www.moneycontrol.com"
response = get(url)
#print(response.text)
soup = BeautifulSoup(response.text,'html.parser')
print(type(soup))
#table=soup.find_all('table',class_="rhsglTbl")
#print(table)
links=soup.find_all('a')
print(links)
for link in links:
    print(link.get('href'))
"""'''lxml'''
print(type(soup))
print(soup.html.head)
print(soup.html.head.meta)"""