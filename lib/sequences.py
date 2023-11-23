#!/usr/bin/env python3

def print_fibonacci(length):
    scheme =[]        
    c = -2
    a = -1
    b = 1
    while len(scheme) < length:
        c = a+b 
        a = b
        b = c
        scheme.append(c)
    pass

    print(scheme)

print_fibonacci(1)