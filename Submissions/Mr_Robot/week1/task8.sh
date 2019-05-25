#!/bin/bash
ssh -R any_port_for_listening:localhost:22 sourceuser@source_ip
ssh user@machine_ip "echo Hi\!"
scp -r /path1/folder user@remotehost:/path2/week1
sftp user@server_ip
export http_proxy="http://USER:PASSWORD@PROXY_SERVER:PORT"
export https_proxy="https://USER:PASSWORD@PROXY_SERVER:PORT"
export ftp_proxy="http://USER:PASSWORD@PROXY_SERVER:PORT"