import requests as req
import json
from bs4 import BeautifulSoup

url 		= "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
page 		= req.get(url)
soup    	= BeautifulSoup(page.text,'html.parser')
tr 			= soup.find_all("tr")
titlecolumn = soup.find_all("td",class_="titleColumn")
ratingcolumn = soup.find_all("strong")

for column in tr:
	for col in column.find_all("strong"):
		if((float)(col.contents[0]) >=8.5 and (float)(col.contents[0]) <=8.8):
			for col in column.find_all('a'):
				print(col.contents[0])