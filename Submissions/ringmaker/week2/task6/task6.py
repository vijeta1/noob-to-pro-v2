import re
import csv
fi=open('access.log','r')
content=fi.readlines()
for line in content:
	s=re.compile('(\d{2}/.*/\d{4}):(\d{2}:\d{2}:\d{2})')
	s=s.search(line)
	group=s.groups()
	if '13/May/2018' in group and group[1]>'12:00:00' and group[1]<'14:52:50':
		print(line)
