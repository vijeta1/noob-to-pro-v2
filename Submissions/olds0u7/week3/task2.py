import requests
import json
import csv

page=requests.get('https://jsonplaceholder.typicode.com/posts')

data=page.json()

f=csv.writer(open('task.csv','w'))
f.writerow(['userId','id','title','body'])

for i in data:
  userId=i['userId']
  id1=i['id']
  title=i['title']
  body=i['body']
  f.writerow([userId,id1,title,body])
 


