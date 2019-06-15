import requests
from bs4 import BeautifulSoup


url="https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

r=requests.get(url)

soup=BeautifulSoup(r.content,'html5lib')

table=soup.find('div',attrs={'class':'lister'})


x=1

for row in table.findAll('td', attrs = {'class':'titleColumn'}):
    print(str(x)+"."+row.a.text)
    x=x+1