#!/bin/bash

echo enter username
read username

echo enter ip of the server
read ipofserver

ssh -R 80:127.0.0.1:8080 $username@$ipoftheserver
