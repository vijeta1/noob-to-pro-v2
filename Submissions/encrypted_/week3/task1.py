import requests

site = "http://www.mocky.io/v2/5b026eb43000007a00cee110"

headers = requests.get(site).headers

print(headers["Flag"])




#output - noobToPro{this_is_basic_flag_}
