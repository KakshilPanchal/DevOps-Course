#/bin/bash

#until loop this loop will coontinoue till your condition become not true till that it will run and if condtion become  true loop end

a=10
until [ $a -eq 1 ]
do 
	echo "value of a is: $a"
	let a--
done
