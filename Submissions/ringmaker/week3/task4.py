import requests

city=input()
url='https://developers.zomato.com/api/v2.1/cities?q='+city
headers={'user-key':'73f76e835eeb99973e7d8d250d514c18'}
page=requests.get(url,headers=headers).json()
city_id=(page['location_suggestions'][0]['id'])
url='https://developers.zomato.com/api/v2.1/search?entity_id=%s&entity_type=city&count=5&sort=rating&order=desc' % city_id
page=requests.get(url,headers=headers)
data=(page.json()['restaurants'])
print('Restraunts')
for some in data:
	rating = float(some['restaurant']['user_rating']['aggregate_rating'])
	if rating > 3:
		print(some['restaurant']['name'])
