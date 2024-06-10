#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 

for line in sys.stdin:
    words = word_pattern.findall(line)
    for word in words:
        print(f"{word.lower()}\t1")
