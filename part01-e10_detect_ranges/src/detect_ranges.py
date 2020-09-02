#!/usr/bin/env python3

def detect_ranges(L):
    lista =  sorted(L)
    newList = []
    i , j= 0, 0
    alku, loppu = 0, 0
    while i < len(lista):
        j = i
        while (j+1)<len(lista):
            if (lista[j]+1) == lista[j+1]:
                loppu = j+1
            else:
                loppu = j
                break
            j = j + 1
        if (j +1) == len(lista):
            loppu = j
        if loppu == alku:
            newList.append(lista[i])
            i = i+1
            alku = alku +1
        else:
            i = j + 1
            newList.extend(list(zip([lista[alku]],[lista[loppu]+1])))#append(range(list[alku],list[loppu]+1))
            alku = loppu + 1
            loppu = alku
    return newList

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
