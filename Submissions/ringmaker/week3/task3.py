import requests
url='https://jsonplaceholder.typicode.com/comments'
page=requests.get(url).json()
email=[]
for some in page:
	recv=some['email']
	if recv not in email:
		email.append(recv)
		print(recv)
