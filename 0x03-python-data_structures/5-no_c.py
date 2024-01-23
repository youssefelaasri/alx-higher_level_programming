#!/usr/bin/python3
def no_c(my_string):
    n_s = ""
    for a in my_string:
        if a == 'c' or a == 'C':
            n_s = n_s + ' '
            continue
        n_s = n_s + a
    return n_s
