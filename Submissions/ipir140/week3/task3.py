import requests
o=requests.get('https://jsonplaceholder.typicode.com/comments')
import json
fi=json.loads(o.text)
email=[]
for i in fi:
   email.append(i['email'])
mylist=list(dict.fromkeys(email))
for i in mylist:
#   print(mylist.index(i),end='. ')
   print(i)
#for i in email:
#   print(email.index(i),end='. ')
#   print(i)
