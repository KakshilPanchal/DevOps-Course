#!/bin/bash

#to maintain log of your script then you can do by usng logger commamnd 
#log file location /var/log/messages

#example
#date | logger 

#logger echo "this file from: ${0}"
#print name of script and it will not show output but in save this script log in /var/log/messages 


#logger "this is information message"

#logger -t "36_NotToprint_Output_of_command.sh" "this is 36 script..."   #log message with tag like your script name with tag



	
shift
	df -h | logger -t "disk usage..."

       
	


