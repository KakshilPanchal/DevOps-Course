#!/bin/bash

#read content from csv file
cat test.csv | awk 'NR!=1 {print}' | while IFS="," read id name age 
do
	echo "id is $id"
	#echo "name is $name"
	#echo "age is $age"
done
#NR! means we dont need first row from csv file number of row
