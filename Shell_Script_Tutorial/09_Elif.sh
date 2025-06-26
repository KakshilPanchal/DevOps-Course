#!/bin/bash
read -p "enter your marks: " marks
if [ $marks -ge 80 ]
then
	echo "First Class with Distinction"
elif [ $marks -ge 60 ]
then
	echo "first Class"
else
	echo "FAIL"
fi

#elif can be add multiple based condition on requirment

#Example

read -p "enter your marks:" count 
if [ $count  -ge 80 ]
then
	echo "First class with distinction"
elif [ $count -ge 55 ]
then
	echo "First Class"
else
	echo "FAIL"
fi
