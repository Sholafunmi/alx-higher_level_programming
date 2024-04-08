#!/usr/bin/python3
"""A txt file to read a function"""

def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
