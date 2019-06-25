import requests

page=requests.get('http://www.mocky.io/v2/5b026eb43000007a00cee110')

print("Flag noobToPro{this_is_basic_flag}")

print(page.headers)
