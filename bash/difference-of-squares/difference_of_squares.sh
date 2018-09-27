#!/usr/bin/env bash

set -e

function square_of_sums() {
  local result=0
  for (( i=1; i<(($1 + 1)); i++ )); do
    (( result+=$i ))
  done
  echo $(( $result**2 ))
}

function sum_of_squares() {
  local result=0
  for (( i=1; i<(($1 + 1)); i++ )); do
    (( result+=($i**2) ))
  done
  echo $result
}

a=$(square_of_sums $1)
b=$(sum_of_squares $1)

case "$2" in
  "")
    echo $(( a - b ))
    ;;
  "-S")
    echo $a
    ;;
  "-s")
    echo $b
    ;;
esac
