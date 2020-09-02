#!/usr/bin/env python3


def main():
    
    for i in range(1,11):
        nelio = square(i)
        kolminkertainen = triple(i)
        if nelio>kolminkertainen:
            break
        print(f"triple({i})=={kolminkertainen} square({i})=={nelio}")
    
def triple(parametri):
    return parametri*3
def square(parametri):
    return parametri**2

if __name__ == "__main__":
    main()
