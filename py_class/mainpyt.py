#!/usr/bin/python3
import sys

add = __import__("main").add
sub = __import__("main").sub
mul = __import__("main").mul
div = __import__("main").div

#or
#from main import *

operant = sys.argv[1]
a = sys.argv[2]
b = sys.argv[3]

if (operant == "add"):
    print(add(int(a), int(b)))
elif (operant == "sub"):
    print(sub(int(a), int(b)))
elif (operant == "null"):
    print(mul(int(a), int(b)))
else:
    print(div(int(a), int(b)))
