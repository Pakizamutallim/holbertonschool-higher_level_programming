#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    else:
        if idx > len(my_list):
            return None
        else:
            return idx
        return my_list[idx]
