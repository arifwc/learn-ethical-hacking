#!/bin/bash

if [ "$1" == "" ]
then
echo 'Lupa ip address boss'
echo 'Syntax : ./ipsweeper.sh XXX.XXX.XXX'

else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep '64 bytes' | cut -d ' ' -f 4 | tr -d ':' &
done
fi
