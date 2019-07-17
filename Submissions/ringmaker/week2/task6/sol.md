```
cat access.log |awk '{if(substr($4,2,11)=="13/May/2018"&&substr($4,14)>"12:00:00"&&substr($4,14)<"14:52:50"){print $0}}'
```
