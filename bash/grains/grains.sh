#!/usr/bin/env bash

set -e

if (( $1 < 1  ||  $1 > 64 )); then
  echo "Error: invalid input" >&2
  exit 1
fi

echo "2^($1-1 )" | bc
