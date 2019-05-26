#!/bin/bash

echo enterpath(like /home/nikhil/Music/nikhil.cpp)
read path


sudo scp -P 2222 -i /home/nikhil/.vagrant.d/insecure_private_key $path vagrant@127.0.0.1:~/week-1
