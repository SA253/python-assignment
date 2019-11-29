from requests import get
from bs4 import BeautifulSoup
url = "http://www.moneycontrol.com"
response = get(url)
soup = BeautifulSoup(response.text,'html.parser')
print(type(soup))
tables=soup.find_all('table',class_="rhsglTbl")
for table in tables:
    links=soup.find('a')
    print(links)
   