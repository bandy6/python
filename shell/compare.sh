#!/bin/bash
echo "please input two number"
read a
read b             
if [ $a -eq $b ]
then  echo "NO.1=NO.2"
elif test  $a -gt $b
then echo "NO.1>NO.2"
else echo "NO.1<NO.2"
fi
