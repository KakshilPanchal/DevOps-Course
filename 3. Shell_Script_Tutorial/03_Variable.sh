#!/bin/bash

#Variables 

name="kakshil panchal" #string
a=10 #integer
age=28 

#To print or use variable Use "$echo" command.
echo "my name is $name and my age is $age year"

#To change the same variable name  value into Different value.
name="Dwait"
echo "My name is $name"

#To store the output of linux command in variable
<< comments
like pwd
date 
hostname
comments
hostname=$(hostname)
echo "The hostname of Machine is:$hostname"

#To define constant value to Variable(It will Not Changed) so  use "readonly" 
readonly constant_value="DevOps"
echo "the constant value for variable is:$constant_value"
#So if you made another same variable then value will Not Changed.

#try to Change the Value of variable After apply costant value to Variable
constant_value="DevOps Enginner"
echo "the value of constant will not changed:$constant_value"
