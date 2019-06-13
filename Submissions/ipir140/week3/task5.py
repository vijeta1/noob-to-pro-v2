import requests
o=requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')
from bs4 import BeautifulSoup
soup=BeautifulSoup(o.text,'lxml')
li=soup.find_all('td', class_='titleColumn')
for t in li:
   print(li.index(t)+1,end='. ') 
   print(t.a.text)


