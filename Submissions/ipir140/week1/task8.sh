echo  "SSH Reverse tunnelling (1) "
echo  "SSH command from local host (2) "
echo  "To copy a folder to a directory named week-1 on remote server (3) "
echo  "SFTP Connection to remote server (4) "
echo  "Proxy export (5) "
echo -n "Enter choice (1-5): "

read c
case $c in
(1)
echo -n "port-no.: "
read port
echo -n "user-id: "
read user
echo -n "server-ip: "
read server_ip
echo "......"
ssh -R $port:localhost:22 $user@$server_ip ;;

(2)
echo "......"
ssh localhost echo -n "..";uname -a; ;;

(3)
echo -n "enter source directory: "
read sdir
echo -n "enter destination source directory: "
read ddir
echo -n "user-id: "
read user
echo -n "server-ip: "
read server_ip
echo "......"
scp -r $sdir $user@$server_ip:$ddir ;;

(4)
echo -n "user-id: "
read user
echo -n "server-ip: "
read server_ip
echo "......"
sftp $user@$server_ip ;;

(5)
echo -n "username: "
read username
echo -n "password: "
read password
export http_proxy="http://username:password@172.31.2.4:8080"
export https_proxy="https://username:password@172.31.2.4:8080"
export ftp_proxy="ftp://username:password@172.31.2.4:8080" ;;

esac
