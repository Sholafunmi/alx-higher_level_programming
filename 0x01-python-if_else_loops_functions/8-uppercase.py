#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            print(chr(ord(i) - 32), end="")
        else:
            print(i, end="")
    print("")
