import requests
import json

url="http://www.mocky.io/v2/5b026eb43000007a00cee110"

response=requests.get(url)


print(response.headers['Flag'])

