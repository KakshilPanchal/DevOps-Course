#!/bin/bash

#If else statement 
#syntax
#if[condition]
#then 
     #statement
#else
     #statement
#fi 
#single condition we used ifelse 

#example
read -p "enter your marks:" marks
if [ $marks -gt 40 ]
then
	echo "PASS"
else 
	echo "FAIL"
fi
