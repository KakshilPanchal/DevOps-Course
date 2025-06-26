#!/bin/bash

FILEPATH="/home/kakshil/Script_Tutorial/demo.txt"

if [ -f $FILEPATH ]  #-f for file exist or not and for -d for Folder exist or not 
then
	echo "file exist"
else
	echo "file not exist"
	echo "creating that file...."
	touch $FILEPATH
fi
