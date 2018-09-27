#!/usr/bin/env bash

set -eu

n=$1
steps=0

if (( n < 1 )); then
  echo "Error: Only positive numbers are allowed"
  exit 1
fi

while [[ $n != 1 ]]; do
  (( steps++ ))
  if (( $n % 2 == 0 )); then
    n=$(( $n / 2 ))
  else
    n=$(( 3 * $n + 1 ))
  fi
done

echo $steps
