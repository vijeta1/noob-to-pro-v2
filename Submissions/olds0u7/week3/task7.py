import requests
from bs4 import BeautifulSoup

page=requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')

soup=BeautifulSoup(page.content,'html.parser')

tv_show=soup.find(class_='lister-list')

tv_show_list=tv_show.find_all(class_='titleColumn')

release_year=input("Input the release year")

for show in tv_show_list:
  if release_year==int(show.span.text):
    print(show.a.text,end=" ")
    print(release_year)
    
    
