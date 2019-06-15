import requests
import json

page=requests.get('https://jsonplaceholder.typicode.com/comments')

data=page.json()

a=[]

for i in data:
  if i['email'] not in a:
    a.append(i['email'])
    
for j in a:
  print(j)
  
