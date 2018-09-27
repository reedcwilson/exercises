#!/usr/bin/env bash

set -e

(( $1 % 3 == 0 )) && result="Pling"
(( $1 % 5 == 0 )) && result=$result"Plang"
(( $1 % 7 == 0 )) && result=$result"Plong"

echo ${result:-$1}
