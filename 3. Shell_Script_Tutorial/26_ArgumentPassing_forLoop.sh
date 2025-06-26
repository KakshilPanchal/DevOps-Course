#!/bin/bash


echo "first argument: $1"
echo "second argument: $2"

echo "number of argument: $#"
echo "all argument value name: $@"

#for loop to access value from arguement
for filename in $@
do 
	echo "copying file: $filename"
done

#this can be also used if suppose you have create script for backup  file then when you run script type file path so that it will backup file based on argument
