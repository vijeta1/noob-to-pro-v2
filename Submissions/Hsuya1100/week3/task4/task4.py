import requests as req
import json
import csv
from bs4 import BeautifulSoup
api_key="321d88f7e609448abf731b180772c14f"
url   = "https://jsonplaceholder.typicode.com/comments"
headers={'user-key':api_key}
page  = req.get(url,headers=headers)
page  = page.json()

# CIty ID fetch
city=input()
urlCity='https://developers.zomato.com/api/v2.1/cities?q='+city
pageCity  = req.get(urlCity,headers=headers)
pageCity  = pageCity.json()
cityID=pageCity['location_suggestions'][0]['id']
print(cityID)

UrlSortRest='https://developers.zomato.com/api/v2.1/search?entity_id=%s&entity_type=city&count=10&sort=rating&order=desc' % cityID
dataPage=req.get(UrlSortRest,headers=headers)
dataPage=dataPage.json()
listRestaurants=dataPage['restaurants']
# print(listRestaurants)
counter=0;
print("City: ",city)
for rest in listRestaurants:
	Rating = float(rest['restaurant']['user_rating']['aggregate_rating'])
	if Rating > 3.0:
		print (counter+1," ",rest['restaurant']['name'],"		Rating: ",Rating)
		counter+=1
	if(counter>=5):
		break
