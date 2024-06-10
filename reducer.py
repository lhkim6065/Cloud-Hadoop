#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None

# Read input from standard input
for line in sys.stdin:
    # Parse the input we got from mapper.py
    word, count = line.strip().split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    # If this is the same word as the current word, increment the count
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write result to standard output
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Output the last word if needed
if current_word == word:
    print(f"{current_word}\t{current_count}")
