#!/usr/bin/env bash

set -e

function get_uniq() {
  echo $(echo "${@/0/}" | grep -o . | perl -ne 'print unless $seen{$_}++' | tr -d '[:space:]')
}

sides=$(get_uniq "${@:2}")

[[ $1 == "equilateral" && ${#sides} == 1 ]] && echo "true" && exit 0
[[ $1 == "isosceles" && ${#sides} < 3 ]] && echo "true" && exit 0
[[ $1 == "scalene" && ${#sides} == 3 ]] && echo "true" && exit 0

echo "false"
exit 1
