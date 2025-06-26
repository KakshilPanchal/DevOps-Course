#!/bin/bash

#sleep command use

read -p "enter the site: " site
ping -c 1 $site
sleep 3s

if [ $? -eq 0 ]  # $? will show previous command is excuted or not ,and 0 means sucessfull executed
	then
		echo "sucessfully executed $site"
	else
		echo "Unsucesful $site"
fi
