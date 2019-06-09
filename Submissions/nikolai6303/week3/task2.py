import requests
import csv

row=['userId','id','title','body']



url="https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)


data = response.json() 

with open('task2.csv','wt') as csvFile:
        writer=csv.writer(csvFile)
        writer.writerow(row)
        for i in range(100):
                userId=data[i]['userId']
                id=data[i]['id']
                title=data[i]['title']
                body=data[i]['body']
                csvData=[[userId,id,title,body]]
                writer.writerow(csvData)
csvFile.close()
