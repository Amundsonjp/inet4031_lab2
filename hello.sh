#!/bin/bash

a=2
b=2
c=$((a + b))
echo "Bash says: Hello, World!"
echo "$a + $b = $c"

myList=("User1" "User2" "User3")
for i in ${!myList[@]}; do
   echo "${myList[$i]}"
done
