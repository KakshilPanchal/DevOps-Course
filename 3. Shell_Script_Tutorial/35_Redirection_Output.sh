#!/bin/bash

ping -c 1 www.google.com > kakshil.log # redirect output  but if you again redirect output with > then old data will remove and new data will be added

pwd > kakshil.log

#so >> using this old data will not removed and new data will be added 
ping -c 1 www.google.com >> kakshil.log
