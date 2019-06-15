from bs4 import BeautifulSoup
import requests

url='https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
page=requests.get(url)
data=BeautifulSoup(page.text,features="lxml")
lis=data.select('td > a')
rate=data.select('td > strong')
movies=[]
for count in range(0,250):
	io=count
	rat=str(rate[io].getText())
	if float(rat) > 8.5 and float(rat) < 8.8:
		name=str(lis[io].getText())
		movies.append(str(name))
for some in movies:
	print(some,end='')
