x=input("Year:")
import requests
o=requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')
from bs4 import BeautifulSoup
soup=BeautifulSoup(o.text,'lxml')
liy=soup.find_all('span', class_='secondaryInfo')
lit=soup.find_all('td', class_='titleColumn')
print("Output:")
for t in lit:
   if int(liy[lit.index(t)].text[1:-1])==int(x):
       print(t.a.text)

