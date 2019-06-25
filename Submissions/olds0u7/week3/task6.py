import requests
from bs4 import BeautifulSoup

page=requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')

soup=BeautifulSoup(page.content,'html.parser')

tv_show=soup.find(class_='lister-list')
tv_show_rating=tv_show.find_all(class_='ratingColumn imdbrating')

tv_show_list=tv_show.find_all(class_='titleColumn')

x=1
a=[]
b=[]

for show in tv_show_rating:
  if float(show.strong.text)<=8.8 and float(show.strong.text)>=8.5:
    a.append(x)
    b.append(float(show.strong.text))
  x=x+1
  
y=1
index=0

for show1 in tv_show_list:
  if y in a:
    print(show1.a.text,end=" ")
    print(b[index])
    index=index+1
  y=y+1 
  
  
