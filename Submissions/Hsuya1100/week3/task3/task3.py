import requests as req
import json
import csv
url   = "https://jsonplaceholder.typicode.com/comments"
page  = req.get(url)
page  = page.json()

emails=[]
for obj in page:
	em=obj["email"]
	if(em not in emails):
		emails.append(em)

print(emails)