#!/bin/bash

echo username
read username

echo ip
read ip

ssh $username@$ip

uname
hostname
