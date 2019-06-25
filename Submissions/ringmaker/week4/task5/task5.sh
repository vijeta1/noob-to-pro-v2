#!/bin/sh
shodan search cisco | awk '{ print $1 }'
