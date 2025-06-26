#!/bin/bash

while IFS="," read id name age #IFS is field seperator means vlaue is seperator by comma 
do
	echo "id is: $id"
	echo "Name is: $name"
	echo "age is: $age"

done < test.csv
