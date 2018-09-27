#!/usr/bin/env bash

set -e

[[ $1 =~ [^GCTA] ]] && { echo 'Invalid nucleotide detected.'; exit 1; }
echo $1 | tr '[GCTA]' '[CGAU]'
