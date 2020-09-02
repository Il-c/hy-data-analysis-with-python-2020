#!/usr/bin/env python3

def distinct_characters(L):
    dictionary ={}
    for item in L:
        dictionary1 = {(item):(len(set(item)))}
        dictionary.update(dictionary1)
    return dictionary

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
