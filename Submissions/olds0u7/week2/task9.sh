
awk '$4 >= "[12/May/2018:08:00:00" && $4 < "[12/May/2018:09:00:00"' access.log | awk  'BEGIN{sum=0;}{sum=sum+$10;} END{print sum;}'
