#!/bin/bash

echo -n "Destination User: "
read USER
echo -n "Destination IP: "
read IP

ssh $USER@$IP "whoami"
echo "Done!"

#result is the $USER
