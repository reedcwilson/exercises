#!/usr/bin/env bash

set -e

total=0
for num in $( echo $1 | grep -o . ); do
  (( total+=$num**${#1} ))
done

[ $total -eq $1 ] && echo "true" || { echo "false"; exit 1; }
