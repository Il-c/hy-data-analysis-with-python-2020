#!/usr/bin/env python3

def find_matching(L, pattern):
    hits = set([])
    for i, x in enumerate(L):
        print(x)
        if pattern in x:
            hits.add(i)

    return list(hits)

def main():
    pass

if __name__ == "__main__":
    main()
