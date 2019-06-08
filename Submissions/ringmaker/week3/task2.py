import requests
import csv

url='https://jsonplaceholder.typicode.com/posts'
page=requests.get(url)

header = ['userId','id', 'title', 'body']
rows = []
page=page.json()
for some in page:
	col=[]
	for one in some:
		col.append(some[one])
	rows.append(col)
print("writing result to task2.csv")
with open('task2.csv', 'wt') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    for row in rows:
        csv_writer.writerow(row)
