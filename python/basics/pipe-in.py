#!/usr/bin/python
import sys

for line in sys.stdin:
    sys.stdout.write(line)
    
# use like this: ps -ef | ./pipe-in.py
