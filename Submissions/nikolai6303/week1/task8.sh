#!/bin/bash
printf 'enter choice 1-5'
read choice



case $choice in
    
1)
echo enter username
read username

echo enter ip of the server
read ipofserver

ssh -R 80:127.0.0.1:8080 $username@$ipoftheserver
 
;;

2)  
echo username
read username

echo ip
read ip

ssh $username@$ip

uname
hostname
;;

3)
echo "enterpath(like /home/nikhil/Music/nikhil.cpp)"
read path


sudo scp -P 2222 -i /home/nikhil/.vagrant.d/insecure_private_key $path vagrant@127.0.0.1:~/week-1
;;

4)
echo remoteserver username
read username

echo ipaddress
read ipaddress

sftp $username@$ipaddress
;;

5)
echo enter user
read user

echo enter password
read pass

echo enter proxy server
read my.proxy.server


export HTTP_PROXY=$user:$pass@$my.proxy.server:8080
export HTTPS_PROXY=$user:$pass@$my.proxy.server:8080
;;

esac


                                                                            
