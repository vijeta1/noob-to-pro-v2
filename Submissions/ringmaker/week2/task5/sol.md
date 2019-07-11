```
cat access.log |sed -n '/404/p' |sed -r 's_Chrome/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+_GoogleBot 3.0_gp'|sed 's/\[//g;s/\]//g' | awk  '{$4=substr($4, 1, length($4)-9); $2=$3=$5=$6=$8=$9=$10=$11=""; print $0}' | sed -n 's/ \{1,\}/,/pg' > new.csv
```
