#!/bin/bash
read -p "Enter Task Number: " num

if [ $num -eq 1 ]
then
	read -p "Enter Username: " username
	read -p "Enter Server IP: " serverip
	read -p "Enter Interface IP:(10.0.0.1) " interfaceip
	read -p "Enter listening port: " lport
	read -p "Enter forwarding port: " fport
	echo "Task 1 is running"
	ssh -R $interfaceip:$lport:127.0.0.1:$fport $username@$serverip
	echo "Task 1 is completed"

fi
if [ $num -eq 2 ]
then
	read -p "Enter Username: " username
	read -p "Enter Server IP: " ip
	read -p "Enter Port Number: " portnum
	read -p "command " comm
	echo "Task 2 is running"
	ssh $username@$ip -p $portnum $comm
	echo "Task 2 is completed"
fi
if [ $num -eq 3 ]
then
	read -p "Enter Username: " username
	read -p "Enter Server IP: " ip
	read -p "Full Folder Path " folder
	read -p "Full Destination Path " dest
	echo "Task 3 is running"
	scp -r $folder $username@$ip:$dest
	echo "Task 3 is completed"
fi
if [ $num -eq 4 ]
then
	read -p "Enter Username: " username
	read -p "Enter Server IP: " ip
	echo "Task 4 is running"
	sftp $username@$ip
	echo "Task 4 is completed"
fi
if [ $num -eq 5 ]
then
	read -p "Enter Username: " uname
	read -p "Enter Password: " pas
	read -p "Enter Proxy: " proxy
	read -p "Enter Proxy Port: " port
	echo "Task 4 is running"
	export HTTP_PROXY=$uname:$pas@$proxy:$port
	export HTTPS_PROXY=$uname:$pas@$proxy:$port
	export FTP_PROXY=$uname:$pas@$proxy:$port
	echo "Task 4 is completed"
fi
