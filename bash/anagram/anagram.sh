#!/usr/bin/env bash

set -e

function sorted() {
  echo $(echo $1 | grep -o . | sort | tr -d '\n')
}

function lowercase() {
  echo $(echo $1 | tr '[A-Z]' '[a-z]')
}

primary=$(lowercase $1)
sorted_primary=$(sorted $primary)

for word in $2; do
  word_lower=$(lowercase $word)
  if [[ 
    $(sorted $word_lower) == $sorted_primary && 
    $word_lower != $primary
  ]]; then
    anagrams="$anagrams $word"
  fi
done

echo $anagrams
