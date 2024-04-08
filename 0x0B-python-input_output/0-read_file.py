#!/usr/bin/python3
"""A txt file to read a function"""

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data)
