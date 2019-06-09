import urllib2
req=urllib2.Request("http://www.mocky.io/v2/5b026eb43000007a00cee110/")
res=urllib2.urlopen(req)
print (res.info() )
res.close();