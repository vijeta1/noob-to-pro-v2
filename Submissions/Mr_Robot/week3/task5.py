import requests
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')
r=requests.get('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250/')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content,"html.parser")
s=soup.find_all("td",class_="titleColumn")
for link in s:
         for d in link.find_all('a'):
              print str(d.contents[0])



