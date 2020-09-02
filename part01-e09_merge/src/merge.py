#!/usr/bin/env python3

def merge(L1, L2):
    list = L1+L2
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
  
    return list

def main():
    pass

if __name__ == "__main__":
    main()
