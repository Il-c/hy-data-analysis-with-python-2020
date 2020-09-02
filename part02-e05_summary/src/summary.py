#!/usr/bin/env python3

import sys
import math

def summary(filename):
    luvut=[]
    summa = 0
    with open(filename, "r") as f:
        for item in f.readlines():
            try:
                luvut.append(float(item))
            except:
                pass
    lukujen_maara = len(luvut)
    average = sum(luvut)/lukujen_maara
    for luku in luvut:
        summa = summa + (luku-average)**2
    sdev = math.sqrt(summa/(lukujen_maara-1))
    return (sum(luvut),average,sdev)

def main():
    for file in sys.argv[1:]:
        tulos = summary(file)
        print(f"File: {file} Sum: {tulos[0]:.6f} Average: {tulos[1]:.6f} Stddev: {tulos[2]:.6f}")
   # for item in list((summary("example.txt"))):
   #     print(f"{item}\t")

if __name__ == "__main__":
    main()
