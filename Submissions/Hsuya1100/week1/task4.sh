#!/bin/bash

echo -n "Destination User: "
read USER
echo -n "Destination IP: "
read IP

sftp $USER@$IP
