#!/usr/bin/python3

class student:
    """This represents a student."""

    def __init__(self, first_name, last_name, age):
    
        """A class that initilozes a new student

        Arg:
            first_name (str): student first name.
            last_name (str): student last name.
            age (int): student age
        """
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
