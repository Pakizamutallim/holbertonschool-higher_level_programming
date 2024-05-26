#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    while num > x:
        try:
            print("{}".format(my_list[num]), end="")
            num += 1
        except IndexError:
            pass
    print("")
    return (num)
