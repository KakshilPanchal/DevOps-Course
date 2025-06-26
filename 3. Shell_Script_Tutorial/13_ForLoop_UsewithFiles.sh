#/bin/bash

#for loop with files

#getting value from file

FILE="/home/kakshil/Script_Tutorial/a.txt"

for name in $(cat $FILE)
do 
	echo "$name"
done
