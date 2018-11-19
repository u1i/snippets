#!/usr/bin/python

# echo hello | ./text2bin.py
import sys

inp = sys.stdin.read()

for x in range(len(inp)-1):
    bs = str(bin(ord(inp[x])))
    print bs.replace('0b',''),
