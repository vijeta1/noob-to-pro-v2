import requests
o=requests.get('https://jsonplaceholder.typicode.com/posts')
import json
fi=json.loads(o.text)
import csv
csvfi=csv.writer(open('task2.csv','w'))
csvfi.writerow(['userId', 'id', 'title', 'body'])
for i in fi:
   csvfi.writerow([ i['userId'], i['id'], i['title'], i['body']])
