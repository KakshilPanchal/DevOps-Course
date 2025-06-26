#!/bin/bash

#exit argument status 

#example


if [ $# -eq 0 ]
then
	echo "please enter atleast One arguements...."
	exit 1
	#this will exit
fi

echo "enter a Full name: $1"

shift
echo "enter a Age: $@"

