### php loose comparison

webpage takes input of number compares it to its md5 hash if they are equal it echo flag <br>
since comparison is `==` it is exploitable <br />
every string in  php starting with 0e and followed by integer is interpreted as 0 <br />
so to pass check we need a string which startswith '0e'+integer and its md5 also starts with '0e'+integer <br />
we write python script
#### difficulty :medium
```
from md5 import md5
st=0
while True:
        m=md5()
        m.update('0e'+str(st))
        g=m.hexdigest()
        if g[:2]=='0e':
                if g[2:].isdigit():
                        print('0e'+str(st))
                        break
        st+=1
```
flag = 'JCTF{d351gn1ng_c7f_15_d1ff1cu17}'
pass= '0e215962017'
