#!/bin/bash

#ARRAY
## array is which used to store n number of value in variable then we used Array

#Syntax:-
#variableName=(1 2 hello "hello kakshil")
#echo "{Array_Name[index_Value]}"

#Example
myArray=(1 2 3 4 5.5 "hey kakshil!")

#to store the value of array then, index of Array start from :0 value.
echo "Value in 5th Index:${myArray[5]}"
echo "Print all Values:${myArray[*]}"

#Find total Lenght or Value in Array 
echo "Length of array:${#myArray[*]}"


#to get specific Value 
echo "second third and fourth print position value is:${myArray[*]:1:5}"

#to Update Array with New Value
myArray+=(8 9 10 "dwait")
echo "value of new Array is:${myArray[*]}"



#How to Store Array key-value Pair means provide key pair for the value 
#STORE VALUE IN KEY PAIR TO ACCESS VALUE USING KEY PAIR.
#syntax
#declare -A <array_Name>
#<array_Name=([])

#Example
declare -A my_Array
my_Array=([name]=kakshil [age]=21 [city]=Ahmedabad)
echo "Name is:${my_Array[name]}"
echo "my age is:${my_Array[age]}"
