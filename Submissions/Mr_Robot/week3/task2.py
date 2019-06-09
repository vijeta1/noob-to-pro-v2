import requests
import urllib2
r=requests.get('https://jsonplaceholder.typicode.com/posts/')
import csv
e=r.json()
rows = []
i=0
for ro in e:
    cols = []
    
    
    for co in ro:
           cols.append(ro[co]) 
    q=cols.pop()
    u=cols.pop()
    b=cols.pop()
    t=cols.pop()
    
    cols.append(u)
    cols.append(b)
    cols.append(q)
    cols.append(t)
    rows.append(cols)
f = csv.writer(open('task3.csv', 'w'))


f.writerow(['|||id|||','userid|||', 'title|||', 'body|||'])
for ro in rows:
     f.writerow(ro)

