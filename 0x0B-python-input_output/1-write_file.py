#!/usr/bin/python3
"""A file writing function"""

def write_file(filename="", text=""):
    """Writes a string to the UTF-8 text file"""

    with open("filename, 'w', encoding='utf-8') as file:
        return file.write(text)
