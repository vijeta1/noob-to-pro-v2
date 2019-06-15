import requests
import urllib2
r=requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250/')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content,"html.parser")

r=soup.find_all("span",class_="secondaryInfo")
print "FOR YEAR 2015\n"
for ra in r:
       k= ra.contents[0]
       if(k=="(2015)" ):
                 
                  o= k.find_previous("a")
                  print str(o.contents[0]) 

