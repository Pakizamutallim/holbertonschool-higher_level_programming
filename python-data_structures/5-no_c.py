#!/usr/bin/python3

def no_c(my_string):
    for i in my_string:
        new_string = ""
        if i != "C" or i != "c":
            new_string += i
    return new_string
