import requests
import json

url="https://jsonplaceholder.typicode.com/comments"

response=requests.get(url)

data=response.json()

unique_values=set()

for item in data:
    unique_values.add(item['email'])

print(unique_values)