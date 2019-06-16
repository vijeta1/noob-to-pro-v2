#! /bin/bash
shodan search Cisco |awk '{print $1}'
