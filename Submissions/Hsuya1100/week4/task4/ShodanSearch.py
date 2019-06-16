import shodan
from bs4 import BeautifulSoup

KEY="Yn8CYuXW9F0UxeXhlpZ7024w9I8ywg3a"
api=shodan.Shodan(KEY)

FACETS=[('org',3),('country',3)]
SEARCH="Apache"
result=api.count(SEARCH,facets=FACETS)
flag=0
print("TOP ORGANISATIONS USING APACHE\n")
for facet in result['facets']:
	for term in result['facets'][facet]:
		print(term['value'],"	   : ",term['count'])
	if flag==0:
		print("TOP COUNTRIES USING APACHE\n")
		flag=1
