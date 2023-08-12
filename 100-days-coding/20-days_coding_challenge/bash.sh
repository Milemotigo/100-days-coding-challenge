#!/bin/bash
#check if arg 2 is empty if empty print

if [ -z "$2" ]
then
	echo "second arg is empty"
else
	echo "second arg is not empty"
fi
