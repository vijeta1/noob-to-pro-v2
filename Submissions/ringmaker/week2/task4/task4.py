import re
import csv
fi=open('access.log','r')
content=fi.readlines()
content=content[20:33]
header=['#', 'ip_addr','date_accessed','endpoint_accessed', 'useragent']
row=[]
count=1
for line in content:
	if 'HTTP/1.1" 404' in line:
		s=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
		p=s.findall(line)
		po=re.compile('\d{1,2}/May/\d{4}')
		r=po.search(line)
		so=re.compile('Mozilla|Safari|Chrome|AppleWebKit')
		de=so.findall(line)
		p.insert(1,r.group())
		if(len(p)==2):
			p.insert(2,'')
		de=" ".join(de)
		p.insert(3,de)
		p.insert(0,count)
		count+=1
		row.append(p)
#print(row)
with open('customers.csv', 'wt') as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(header) # write header

    for rows in row:
        csv_writer.writerow(rows)
