#!/usr/bin/env python

import re


def get_words(phrase):
    r = re.compile("([a-z0-9]+)('?[a-z0-9]+)*")
    return [a + b for a, b in r.findall(phrase)]


def word_count(phrase):
    counts = {}
    for word in get_words(phrase.lower()):
        counts[word] = counts.get(word, 0) + 1
    return counts
