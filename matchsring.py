import re
import sys
prog = re.compile('(a|b)*$')
s=str(input())
if prog.match(s):
    print ("yes")
else:
    print ("no")
