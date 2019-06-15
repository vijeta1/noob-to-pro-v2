import requests
from bs4 import BeautifulSoup


url="https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

r=requests.get(url)

soup=BeautifulSoup(r.content,'html5lib')

table=soup.find('div',attrs={'class':'lister'})

#print(div)

x=1
thiset=set()

for row in table.findAll('td', attrs = {'class':'ratingColumn imdbRating'}):
    if(float(row.strong.text)>=8.5 and float(row.strong.text)<=8.8):
        thiset.add(x)
    x=x+1

y=1
z=1

for row in table.findAll('td', attrs={'class': 'titleColumn'}):
    if y in thiset:
        print(str(z)+'.'+row.a.text)
        z=z+1
    y=y+1
