echo -n "port-no. :"
read port
echo -n "user-id :"
read user
echo -n "server-ip :"
read server_ip
echo "......"
ssh -R $port:localhost:22 $user@$server_ip
