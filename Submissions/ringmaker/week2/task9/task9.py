import re
import csv
fi=open('access.log','r')
content=fi.readlines()
ans=0

for line in content:
	s=re.compile('(\d{2}/.*/\d{4}):(\d{2}:\d{2}:\d{2})')
	s=s.search(line)
	group=s.groups()
	if '12/May/2018' in group and group[1]>'08:00:00' and group[1]<'09:00:00':
		s=re.compile(' HTTP/1.\d" \d{3} (\d{2,10})')
        	s=s.search(line)
		ans+=int(s.groups()[0])
print(ans)
