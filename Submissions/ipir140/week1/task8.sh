echo  "SSH Reverse tunnelling (1) "
echo  "SSH command from local host (2) "
echo  "To copy a folder to a directory named week-1 on remote server (3) "
echo  "SFTP Connection to remote server (4) "
echo  "Proxy export (5) "
echo -n "Enter choice (1-5): "

read c
case $c in
(1)
ssh -R 20001:localhost:30001 root@192.168.43.108 ;;

(2)
echo "......"
ssh localhost uname -a; ;;

(3)
scp -r /home/myserver/folder ipir140@192.168.43.108:/home/remote/week-1;;

(4)
sftp ipir140@192.168.42.121 ;;

(5)
export http_proxy="http://username:password@172.31.2.4:8080"
export https_proxy="https://username:password@172.31.2.4:8080"
export ftp_proxy="ftp://username:password@172.31.2.4:8080" ;;

esac
