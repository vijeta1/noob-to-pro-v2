import requests
import urllib2

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import unicodedata
r=requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250/')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content,"html.parser")

r=soup.find_all("td",class_="ratingColumn imdbRating")
for ra in r:
       k= ra.contents[1:2]
       for rating in ra.find_all('strong'):
           e=rating.contents[0]
           if(float(e) >=8.5 and float(e)<=8.8 ):
                               
                  o= e.find_previous("a")
                  print str(o.contents[0])
                 



