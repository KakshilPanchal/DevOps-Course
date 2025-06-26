#!/bin/bash 

#Case 
#switch Case 

#ask question to user like if u press A then you will get (date) as Output like that 

#syntax 
#case <variable_name> in
             #a)date;;
	     #b)ls;;

echo " provide an option"
echo " Press D for print Date"
echo " Press L for list Scripts"
echo " Type pwd  to check current Location"
echo " type ls -l to display detail information of file and folder in current location"
echo " Press P  display today is which day and which date"


read -p "enter something:" choice 
case $choice in
	D)date;;
	L)ls;;
	pwd)pwd;;
	ls-l)
		echo "In Current location"
		ls -l  
		echo "Ending..."
		;;
	P)date +%A-%D;;	
	*) echo "Plase enter a Correct value"  #*) if user enter wrong value
esac

