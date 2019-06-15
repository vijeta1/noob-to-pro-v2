import requests
from bs4 import BeautifulSoup

page=requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')

soup=BeautifulSoup(page.content,'html.parser')

tv_show=soup.find(class_='lister-list')

tv_show_list=tv_show.find_all(class_='titleColumn')

for show in tv_show_list:
  print(show.a.text)
  
  
