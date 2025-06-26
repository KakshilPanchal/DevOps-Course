#!/bin/bash

function myfun {
num1=$1
num2=$2
let sum=$num1+$num2
echo "Sum of num1 and num2 is: $sum"

}
myfun 5 1 
myfun 10 1

