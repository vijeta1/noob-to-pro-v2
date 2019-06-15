import requests as req
import json
import csv
url  = "https://jsonplaceholder.typicode.com/posts"
page = req.get(url)
page = page.json()

data      = open('data.csv','w')
csvwriter = csv.writer(data)

c=0
for obj in page:
	if(c==0):
		csvwriter.writerow(obj.keys())
		c+=1
	csvwriter.writerow(obj.values())