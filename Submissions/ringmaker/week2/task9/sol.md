```
cat access.log |awk '{if(substr($4,2,11)=="13/May/2018"&&substr($4,14)>"08:00:00"&&substr($4,14)<"09:00:00"){i+= $10}}END{print i}'
```