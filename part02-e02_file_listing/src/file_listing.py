#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    filelista=[]
    with open(filename, "r") as f:
        for line in f:
            lista = re.findall(r'(\d{2,})\s([A-Z][a-z]{2,2})\s+(\d{1,2})\s(\d\d)\:(\d\d)\s(\w*.\w+.?\w*)',line)
            print(lista)
            if len(lista)==0:
                continue
            temp=list(lista[0])
            temp[0]=int(temp[0])
            temp[2]=int(temp[2])
            temp[3]=int(temp[3])
            temp[4]=int(temp[4])
           
            filelista.append(tuple(temp))
            
    return filelista

def main():
    print(file_listing("listing.txt"))

if __name__ == "__main__":
    main()
