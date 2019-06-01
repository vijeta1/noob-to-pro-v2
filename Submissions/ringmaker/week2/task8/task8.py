import re
import csv
fi=open('access.log','r')
content=fi.readlines()
for line in content:
	s=re.compile(' HTTP/1.\d" \d{3} (\d{2,10})')
	s=s.search(line)
	print(s.groups()[0])
