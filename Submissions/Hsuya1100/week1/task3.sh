#!/bin/bash

echo -n "Destination User: "
read USER
echo -n "SOURCE: "
read SOURCE
echo -n "DESTINATION: "
read DESTINATION
scp -r $SOURCE $USER@localhost:$DESTINATION
echo "Done !"
