#!/usr/bin/env bash

set -e

for word in ${1/-/ }; do
  acronym=${acronym}${word:0:1}
done

echo $acronym | tr '[a-z]' '[A-Z]'
