!#bin/bash

echo "select options 1 to 5"

read OPTION

if [ "$OPTION" -eq 1 ] 
then
echo -n "Listeining Port: "
read PORT
echo -n "Destination User: "
read USER
echo -n "Destination IP: "
read IP

ssh -L $PORT:localhost:30301 $USER@$IP
echo "Done !"

elif [ "$OPTION" -eq 2 ]
then

echo -n "Destination User: "
read USER
echo -n "Destination IP: "
read IP

ssh $USER@$IP "whoami"
echo "Done!"


elif [ "$OPTION" -eq 3 ]
then
echo -n "Destination User: "
read USER
echo -n "SOURCE: "
read SOURCE
echo -n "DESTINATION: "
read DESTINATION
scp -r $SOURCE $USER@localhost:$DESTINATION
echo "Done !"



elif [ "$OPTION" -eq 4  ]
then

echo -n "Destination User: "
read USER
echo -n "Destination IP: "
read IP

sftp $USER@$IP



elif [ "$OPTION" -eq 5 ] 
then

#USE sudo to run file
#Collecting required info

echo "host"
read host
echo "port"
read port
echo "Username"
read User
echo "Password"
read -s Password

Proxy="http://$User:$Password@$host:$port/"

#setting up proxy

export http_proxy=$Proxy
export https_proxy=$Proxy
export ftp_proxy=$Proxy
export all_proxy=$Proxy
export socks_proxy=$Proxy

export HTTP_PROXY=$Proxy
export HTTPS_PROXY=$Proxy
export FTP_PROXY=$Proxy
export ALL_PROXY=$Proxy
export SOCKS_PROXY=$Proxy

else
  echo "Incorrect Input"
 fi
