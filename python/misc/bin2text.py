#!/usr/bin/python

import fileinput

for line in fileinput.input():
    b = '0b' + line
    print chr(int(b,2))


echo "01010011
01101101
01100001
01110010
01110100
01100001
01110011
01110011
00100000
01111001
01101111
01110101
00111010
00101001" | ./bin2text.py
