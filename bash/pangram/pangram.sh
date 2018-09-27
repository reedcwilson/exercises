#!/usr/bin/env bash

set -e

alpha="abcdefghijklmnopqrstuvwxyz"
str=$(echo $1 | tr '[A-Z]' '[a-z]' | grep -o . | sort | uniq | tr -cd '[a-z]')
exit $(( ${#alpha} != ${#str} ))
