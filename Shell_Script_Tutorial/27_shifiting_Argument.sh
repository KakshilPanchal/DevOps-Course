#!/bin/bash

#shifting argument is used when you pass multiple argument and we can shift the argument

#Example
#to create user. provide username and Description

echo "creating User....."
echo "Username $1"
shift
echo "description $@"
echo "Number of argument are... $#"

