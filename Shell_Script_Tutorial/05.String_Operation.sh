#!/bin/bash

#String Operation#


myvar="my name is kakshil panchal"  #string
#now here we add variable and it value into another variable 
myvarLength=${#myvar}
echo "length of varibale is $myvarLength"
echo "length is ${#myvar}"

#Upper
echo "uppercase is:-------${myvar^^}"   #for upper use ^^

#Lower 
echo "lowercase is:-------${myvar,,}"    #for Lower case ,,

#Replace 
echo "Replace word is: ---- ${myvar/panchal/miteshbhai Panchal}"   # for replace use old_name/new_name

#slice 
echo "slice is: ---- ${myvar:3:23}"  #want specific  word using slice :<starting character(index no. start from:0>:<length of character>(start from 1)

