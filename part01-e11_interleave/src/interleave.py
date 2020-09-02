#!/usr/bin/env python3

def interleave(*lists):
    newList = []
    i = 0;
    zippedList = list(zip(lists))
    while i < len(lists[0]): 
        #Käydään läpi alkio i joka listasta ja lisätään palautettavaan listaan
        for item in zippedList:
            y = list(item)
            x = y[0]
            newList.append(x[i])
        i += 1
    return newList

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
