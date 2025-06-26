#!/bin/bash

#using Continue in loop
#continue will skip that loop if match is found and print next value

var=6
for k in 1 2 3 4 5 6 7 8 9 10
do
	if [ $var -eq  $k ]
	then
		echo "MATCHED FOUND $k"
		continue 
	else
		echo "NOT FOUND $k"
	fi
done
