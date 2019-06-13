import requests
o=requests.get('http://www.mocky.io/v2/5b026eb43000007a00cee110')
headers=o.headers
print("flag:   "+str(o.headers['flag']),end="\n\n")
print("headers:   "+str(o.headers))
