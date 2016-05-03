#!/bin/bash

if [ -z $1 ]; then
	read -p "username: " usrname
	read -s -p "password: " passwd
	echo
	$0 $usrname $passwd &
	exit 0
else
	usrname=$1
	passwd=$2
fi

while true; do
	python ruclogin.py $usrname $passwd
	sleep 36000
done
