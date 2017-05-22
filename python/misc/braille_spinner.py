#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import time,sys

braille = ['⣽','⢿','⣻','⡿','⣾','⣟','⣯','⣷']

z = len(braille)

for x in range(10):
	r = (randint(0,z-1))
	sys.stdout.write("Working " + braille[r] + " " + str(x*10) + "% done" )
	sys.stdout.flush()

	time.sleep(1)
	sys.stdout.write("\r")
	sys.stdout.flush()

sys.stdout.write("Working " + braille[r] + " " + "100 % done" )
print "\nCompleted."
