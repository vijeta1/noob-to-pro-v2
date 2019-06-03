#!/bin/bash
for((; ;))
do
   echo "what you want to do"
   echo "1:reverse tunnelling  2:writing to remote server   3:copying folder to remote server 4:connecting to server using sftp 5:setting proxy 6:exit"

   echo "enter choice "
   read var
   if[$var == '6']
   then
       break
   elif[$var =='1']
   then 
      echo "first doing reverse tunnelling"
      read sourceuser
      read source_ip
      ssh -R any_port_for_listening:localhost:22 $sourceuser@$source_ip
   elif[$var =='2']
   then
      read user
      read machine_ip 
      echo "executing command remotely to echo Hi on remote server  "
      ssh $user@$machine_ip "echo Hi\!"
    
   elif[$var =='3']
   then 
      echo "copying folder1 from local host to remote server directory week1 "
      scp -r folder1 host2@192.168.42.22:/home/host2/week1

   elif[$var =='4']
   then
     read user
     read server_ip 
     echo "connecting to server using sftp"
     sftp $user@$server_ip
   elif[$var =='5']
   then
        read USER  
        read PASSWORD 
        read PROXY_SERVER
        read PORT

       echo "setting up proxy using export command "
       export http_proxy="http://$USER:$PASSWORD@$PROXY_SERVER:$PORT"
       export https_proxy="https://$USER:$PASSWORD@$PROXY_SERVER:$PORT"
       export ftp_proxy="http://$USER:$PASSWORD@$PROXY_SERVER:$PORT"

  fi
done
 