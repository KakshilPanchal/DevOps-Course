#!/bin/bash


#here we change the make code dynamic means change the value in code using arguments in function also
function Myfun {
	echo "--------"
	echo "welcome $1" #$1 if first argument
	echo "--------"
        echo "hello good morning $1"
        echo "-------"
        echo "welcome $2"
        echo "-------"
        echo "hello good morning $2"	
}
Myfun kakshil kakshil
Myfun dwait

#remember you need to provide value to argument
