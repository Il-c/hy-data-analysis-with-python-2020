#!/usr/bin/env python3

def reverse_dictionary(d):
    
    revDict = d.copy()
    d.clear()
    for key, value in revDict.items():
        for i in value:
            if i in d:               
                d[i].append(key)
            else:
                d.update({i:[key]})

    return d

def main():
    pass

if __name__ == "__main__":
    main()
