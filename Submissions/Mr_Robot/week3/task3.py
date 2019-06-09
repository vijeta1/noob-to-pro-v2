import requests
import urllib2
import json
r=requests.get('https://jsonplaceholder.typicode.com/comments/')
from bs4 import BeautifulSoup
d=r.json()

set1=set() 
for row in d:
      set1.add(row['email'])
for i in set1:
     print i

