#!/usr/bin/env python3
import sys
import re

word_pattern = re.compile(r'\b[a-zA-Z]+\b')

for line in sys.stdin:
    words = word_pattern.findall(line)
    for word in words:
        print(f"{word.lower()}\t1")
