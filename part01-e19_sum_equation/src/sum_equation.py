#!/usr/bin/env python3

def sum_equation(L):
    list = " + ".join([str(x) for x in L])
    if len(list)==0:
        list = "0"
    list = list + " = "+str(sum(L))
    return list

def main():
    print(sum_equation([1,5,7]))
    print(sum_equation([]))

if __name__ == "__main__":
    main()
