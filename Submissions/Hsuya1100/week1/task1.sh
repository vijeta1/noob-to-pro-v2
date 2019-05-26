#!/bin/bash
echo -n "Listeining Port: "
read PORT
echo -n "Destination User: "
read USER
echo -n "Destination IP: "
read IP

ssh -L $PORT:localhost:30301 $USER@$IP
echo "Done !"
