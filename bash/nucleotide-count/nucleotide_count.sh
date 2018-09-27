#!/usr/bin/env bash

set -e

if [[ $1 =~ [^ACGT] ]]; then
  echo "Invalid nucleotide in strand"
  exit 1
fi

declare -A nucleotides=( [A]=0 [C]=0 [G]=0 [T]=0 )

for n in $(echo $1 | grep -o .); do
  (( nucleotides[$n]=${nucleotides[$n]} + 1 ))
done

for n in "${!nucleotides[@]}"; do
  echo "$n: ${nucleotides[$n]}"
done
