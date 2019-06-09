grep -i 'post' access.log

or

awk '{IGNORECASE=1} /post/ {print}' access.log
