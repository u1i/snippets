from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
The function eprint can be used in the same way as the standard print function:

>>> print("Test")
Test
>>> eprint("Test")
Test
>>> eprint("foo", "bar", "baz", sep="---")
foo---bar---baz
