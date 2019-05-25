#!/bin/bash

echo enter user
read user

echo enter password
read pass

echo enter proxy server
read my.proxy.server


export HTTP_PROXY=$user:$pass@$my.proxy.server:8080
export HTTPS_PROXY=$user:$pass@$my.proxy.server:8080
