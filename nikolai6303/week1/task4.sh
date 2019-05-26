#!/bin/bash

enter remoteserver username
read username

enter ipaddress
read ipaddress

sftp $username@$ipaddress
