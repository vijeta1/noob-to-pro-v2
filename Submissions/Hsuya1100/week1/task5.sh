#!/bin/bash

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

