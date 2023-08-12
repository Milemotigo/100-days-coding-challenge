#!/bin/bash

input="$1"

# Split the input using the dot delimiter
awk -F '.' '{print "The subdomain " $1 " is a " $4 " record and points to " $5}' <<< "$input"
