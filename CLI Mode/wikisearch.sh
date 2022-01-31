#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
fi

LINK="https://en.wikipedia.org/wiki/$1"

echo -ne '##########                (50%)\r'
sleep 1
echo -ne '#######################   (100%)\r'
echo -ne '\n'

if [[ -f "log.txt" ]]
then
    echo "$1	$LINK" >> log.txt

else
	touch log.txt
	echo "$1	$LINK" >> log.txt
fi


echo "Below is Your required Link	All your queries are gettin saved in 'log.txt'"
echo $LINK
