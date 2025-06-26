#!/bin/bash

#example of Break in Loop
#break = it will break the loop if condition is meet

#Example

var=6
for i in 1 2 3 4 5 6 7 8 9
do
	if [ $var -eq $i ]
	then
		echo "Match Found"
		break
	fi
	echo "Not found $i"
done
