#!/usr/bin/python3

def uppercase(str):
    for i in str:
        res = ord(i)
        if res >= 97 and res <= 122:
            res = res - 32
        print("{}".format(chr(ord(i) - 32)), end="")
    print()
