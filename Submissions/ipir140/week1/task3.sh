echo -n "enter source directory:"
read sdir
echo -n "enter destination source directory:"
read ddir
echo -n "user-id :"
read user
echo -n "server-ip :"
read server_ip
echo "......"
scp -r $sdir $user@$server_ip:$ddir
