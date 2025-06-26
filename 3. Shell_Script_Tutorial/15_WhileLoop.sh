#/bin/bash

#while loop will continoue till your condition is ture if condition become false loop will be end
count=0
num=10
while [ $count -le $num ]
do
	echo "number is $count"
	let count++
done
