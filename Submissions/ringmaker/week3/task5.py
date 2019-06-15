from bs4 import BeautifulSoup
import requests

url='https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
page=requests.get(url)
data=BeautifulSoup(page.text,features="lxml")
data=data.select('td > a')
for some in data:
	name=some.getText()
	print(name,end='')
