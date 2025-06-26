#!/bin/bash

read -p "enter a website name: " site 

ping -c 1 $site >> /dev/null #/dev/null use if you dont want to redirect and not to print output in terminal
sleep 3s

if [ $? -eq 0 ]
then
	echo "Sucessfully Connected........ $site"
else
	echo "Unable to connect!!!! $site"
fi
