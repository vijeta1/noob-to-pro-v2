#!/bin/bash
#read NAME
#lis="jisha kjk dsfsdf"
#for NAME in $(cat file) ;do
#	echo "${NAME}"
#done
VAR=1
while(VAR==1)
do
echo "enter task no to perform"
read TASK
case $TASK in
	1) echo "enter user";read USER;echo "enter ip";read IP ;echo "password";read PASS;echo "port" ;read PORT;echo "connecting";ssh -N -f -T -R 2222:localhost:22 ${USER}@${IP} -p${PORT};echo "$PASS";;
	2) echo "enter user";read USER;echo "enter ip";read IP;echo "password";read PASS;echo "port"  ;read PORT;echo "command to execute";read COMMAND;ssh ${USER}@${PORT} -p ${PORT} ${COMMAND};echo "$PASS";;
	3) echo "enter user";read USER;echo "enter ip";read IP;echo "port"  ;read PORT;scp -P${PORT} -r ./week1/ ${USER}@${IP}:.;;
	4) echo "enter user";read USER;echo "enter ip";read IP;echo "port"  ;read PORT;echo "file path to copy"; read LOC1;echo "path to copy";read LOC2;sftp -P${PORT} ${USER}@${IP}:${LOC1} ${LOC2};;
	5) read JOB;
		if [ "$JOB" == "set" ];
		then
		(echo "enter user";read USER;echo "enter proxy ip";read PROXY;echo "port"  ;read PORT;set http_proxy='http://${USER}:${PASS}@${PROXY}:${PORT}';set https_proxy='http://${USER}:${PASS}@${PROXY}:${PORT}';set ftp_proxy='http://${USER}:${PASS}@${PROXY}:${PORT}')
		else
		(unset http_proxy;unset https_proxy;unset ftp_proxy)
		 fi;;
esac
done
