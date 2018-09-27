#!/usr/bin/env bash

set -e

function getPoints() {
  case "$1" in
    "a" | "e" | "i" | "o" | "u" | "l" | "n" | "r" | "s" | "t")
      echo 1
      ;;
    "d" | "g")
      echo 2
      ;;
    "b" | "c" | "m" | "p")
      echo 3
      ;;
    "f" | "h" | "v" | "w" | "y")
      echo 4
      ;;
    "k")
      echo 5
      ;;
    "j" | "x")
      echo 8
      ;;
    "q" | "z")
      echo 10
      ;;
  esac
}

word=$(echo $1 | awk '{print tolower($0)}')

total=0
for (( i = 0; i < ${#word}; i++ )); do
  total=$((total + $(getPoints ${word:$i:1})))
done

echo $total
