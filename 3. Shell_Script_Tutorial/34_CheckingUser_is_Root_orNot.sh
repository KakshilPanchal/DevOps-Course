#!/bin/bash

#check user is root or not
#0 for root
#if 0 is not display then it is not root user 

#Example
if [ $UID -eq 0 ]  # $UID command for check user is root or not
then
	echo " User is root"

else
	echo " User is Not Root"
fi
