#!/usr/bin/env python3

def transform(s1, s2):
    result = list((x*y) for x,y in list(zip(map(int,s1.split()),map(int, s2.split()))))
    return result

def main():
    pass

if __name__ == "__main__":
    main()
