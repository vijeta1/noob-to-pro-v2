import requests
o=requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')
from bs4 import BeautifulSoup
soup=BeautifulSoup(o.text,'lxml')
lir=soup.find_all('td', class_='ratingColumn imdbRating')
rst=[]
for r in lir:
    if float(r.strong.text)<=8.8:
       if float(r.strong.text)>=8.5:
          rst.append(lir.index(r))
q=0
lit=soup.find_all('td', class_='titleColumn')
for t in lit:
   if int(lit.index(t))==int(rst[q]):
       print(q+1,end='. ')
       print(t.a.text)
       q+=1
       if(q==len(rst)):
         break

