#!/bin/bash

#logical operator can used in conditional statment


# Two type of condition
#01- &&(AND) --> both condition True-->True If not then False
#2- ||(OR) --> If any condition is True then true if both False then it will be False

#Example
aadhar_num=0
read -p "enter your age " age
read -p "your country ? " country
read -p "you have Aadhar card Press Yes or No: " aadhar
	
if [ $age -ge 18 ] && [ $country == "india" ] || [ $aadhar == "yes" ]  #for numerical use -ge and for String we use ==
then
 echo "eligible for vote"	
else 
	echo "Not Eligible"
fi
			 
#example
Age=13
[ $Age -ge 18 ] && echo "Adult" || echo "minor"


