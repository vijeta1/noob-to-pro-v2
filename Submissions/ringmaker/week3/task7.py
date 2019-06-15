from bs4 import BeautifulSoup
import requests
print("enter year whose movies u want")
year=int(input())
url='https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
page=requests.get(url)
data=BeautifulSoup(page.text,features="lxml")
lis=data.select('td > a')
rate=data.findAll('span',{'class':'secondaryInfo'})
for count in range(0,250):
	io=count
	movie_year=str(rate[io].getText())
	movie_year=int(movie_year.strip('(|)'))
	if movie_year==year:
		name=str(lis[2*io+1].getText())
		print(name)
