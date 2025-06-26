#!/bin/bash 


#Arithmetic Operation MATHS

x=10
y=2

#mutliplication 
#using let command 

let multiply=$x*$y
echo "multiplication is:$multiply"

let sum=$x+$y
echo "addition is: $sum"

echo "substraction is:$(($x-$y))"   # you can write also by doing this instead of making new variable and store value and print value
# or you can do by this also for addition like ((sum++))

echo "addition is:$((++x))"  #by default increment by +1
echo "decrement is $((--x))" #decrementr by -1
echo "decrement for y: $((--y))" 

