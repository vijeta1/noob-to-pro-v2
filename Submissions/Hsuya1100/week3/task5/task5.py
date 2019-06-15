import requests as req
import json
from bs4 import BeautifulSoup

url 		= "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
page 		= req.get(url)
soup    	= BeautifulSoup(page.text)
titlecolumn = soup.find_all("td",class_="titleColumn")

counter = 1
for column in titlecolumn:
	for col in column.find_all('a'):
		print(counter,". ",col.contents[0])
		counter+= 1