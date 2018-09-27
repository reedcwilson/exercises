#!/usr/bin/env bash

set -e

if [ $# -eq 0 ]; then
  echo "Usage: hamming.sh <string1> <string2>"
  exit 1
elif [ ${#1} -ne ${#2} ]; then
  echo "The two strands must have the same length."
  exit 1
fi

diff=0
for (( i=0; i<${#1}; i++ )); do
  (( diff+=$([ ${1:$i:1} == ${2:$i:1} ] && echo 0 || echo 1) ))
done
echo $diff
