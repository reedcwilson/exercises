
import re


def abbreviate(words):
    return ''.join(re.findall(r'\b(\w)', words)).upper()
