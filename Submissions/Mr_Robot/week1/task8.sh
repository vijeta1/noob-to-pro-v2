#!/bin/bash

echo "first doing reverse tunnelling"
ssh -R any_port_for_listening:localhost:22 sourceuser@source_ip

echo "executing command remotely to echo Hi on remote server  "
ssh user@machine_ip "echo Hi\!"

echo "copying folder1 from local host to remote server directory week1 "
scp -r folder1 host2@192.168.42.22:/home/host2/week1

echo "connecting to server using sftp"
sftp user@server_ip

echo "setting up proxy using export command "
export http_proxy="http://USER:PASSWORD@PROXY_SERVER:PORT"
export https_proxy="https://USER:PASSWORD@PROXY_SERVER:PORT"
export ftp_proxy="http://USER:PASSWORD@PROXY_SERVER:PORT"