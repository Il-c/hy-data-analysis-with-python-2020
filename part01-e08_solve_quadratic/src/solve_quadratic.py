#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    first =(-b+(math.sqrt(b**2-4*a*c)))/(2*a)
    second = (-b-(math.sqrt(b**2-4*a*c)))/(2*a)
    result = (first,second)
    return (first,second)

def main():
    #pass
    print(solve_quadratic(-2,2,1))

if __name__ == "__main__":
    main()
