#!/usr/bin/env python

import sys

def sqrt(x):
    guess = x
    i = 0 
    while guess*guess != x and i < 20:
        guess = (guess +x / guess)/2.0
        i += 1
    return guess

def main():
    try:
        print(sqrt(3))
    except ZeroDivisionError:
        print("Cannot compute square numbers for negative numbers")

if __name__ == "__main__":
    main()