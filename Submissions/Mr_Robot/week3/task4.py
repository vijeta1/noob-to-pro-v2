import requests
print "enter city"
city=str(raw_input())
import sys
reload(sys)
sys.setdefaultencoding('utf8')

cityend='https://developers.zomato.com/api/v2.1/cities?q='+city
#print city
r=requests.get(cityend,headers={'user-key': '7c71d5d579bb1b5d84935aa6f98f2ec6'})
citypage=r.json()
#print citypage
cityid=(citypage['location_suggestions'][0]['id'])
resultlink='https://developers.zomato.com/api/v2.1/search?entity_id=%s&entity_type=city&count=10&sort=rating&order=desc' % cityid
resultpage=requests.get(resultlink,headers={'user-key':'7c71d5d579bb1b5d84935aa6f98f2ec6'})
resultpage=resultpage.json()
#print resultpage
restrauntslist=(resultpage['restaurants'])
i=0
for r in restrauntslist:
	aggrating = float(r['restaurant']['user_rating']['aggregate_rating'])
	if aggrating > 3.0:
         print str(r['restaurant']['name'])
         i=i+1
         if(i==5):
             break
