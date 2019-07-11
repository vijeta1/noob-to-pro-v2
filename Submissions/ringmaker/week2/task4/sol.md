```
cat access.log |sed -n '/404/p' |sed -n '20,33p' |sed 's/\[//g;s/\]//g' | awk  '{$4=substr($4, 1, length($4)-9); $2=$3=$5=$6=$8=$9=$10=$11=""; print $0}' | sed -n 's/ \{1,\}/,/pg' > new.csv
```
