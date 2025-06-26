#!/bin/bash

#to read content from file using while loop

while read myvar
do
	echo $myvar
done < a.txt
