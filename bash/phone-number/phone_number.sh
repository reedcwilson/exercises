#!/usr/bin/env bash

set -e

num=$(echo $1 | tr -dc '[:digit:]')

if [[ ! $num =~ ^1?[2-9][0-9]{2}[2-9][0-9]{6}$ ]]; then
  echo "Invalid number.  [1]NXX-NXX-XXXX N=2-9, X=0-9"
  exit 1
fi

[[ ${#num} == 11 ]] && echo ${num:1} || echo $num
