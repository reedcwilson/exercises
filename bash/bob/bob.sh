#!/usr/bin/env bash

set -e

sentence=$(echo $1 | tr -d '[:space:]')

shout_str=$(echo $sentence | tr -dc '[:alpha:]')

[[ ! $shout_str =~ [a-z]+ && ! -z $shout_str ]] && is_yell=0
[[ "$sentence" == *\? ]] && is_question=0

if [ -z "$sentence" ]; then
  echo "Fine. Be that way!"
elif [[ $is_yell == 0 && $is_question == 0 ]]; then
  echo "Calm down, I know what I'm doing!"
elif [[ $is_question == 0 ]]; then
  echo "Sure."
elif [[ $is_yell == 0 ]]; then
  echo "Whoa, chill out!"
else
  echo "Whatever."
fi
