grep -v -i 'chrome' access.log

or

awk '{IGNORECASE=1} !/chrome/ {print}' access.log
