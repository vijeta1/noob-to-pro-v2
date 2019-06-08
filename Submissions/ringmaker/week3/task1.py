
import requests
url='http://www.mocky.io/v2/5b026eb43000007a00cee110'
page=requests.get(url)
print(page.text)
