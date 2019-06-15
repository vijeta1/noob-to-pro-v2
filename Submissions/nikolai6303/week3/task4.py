import requests
from pprint import pprint

city=input("enter city name")

cityapi="https://developers.zomato.com/api/v2.1/cities?q="+city
header = {"user_key": "e8285ce31e9e760e37bd893feeece5e3"}


responsea = requests.get(cityapi, headers=header)

dataa=responsea.json()

cityid=dataa['location_suggestions']
cityida=cityid[0]
cityidfinal=cityida['id']

restaurantapi="https://developers.zomato.com/api/v2.1/search?entity_id="+str(cityidfinal)+"&entity_type=city"
responseb=requests.get(restaurantapi, headers=header)


Dict={}

datab=responseb.json()
restaurant=datab['restaurants']
for rate in restaurant:
    rating = float(rate['restaurant']['user_rating']['aggregate_rating'])
    if rating >3:
        name=rate['restaurant']['name']
        Dict[name]=rating

        
for x in range(5):
        max =0
        for key,value in Dict.items():
                if(max<value):
                        max=value
                        resta=key 
        Dict.pop(resta)
        print(resta, "=>", max)              