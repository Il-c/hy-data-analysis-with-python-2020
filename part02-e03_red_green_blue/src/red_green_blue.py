#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    
    with open(filename, "r") as f:
        result=[]
        taulukko = f.readlines()
        taulukko.pop(0)
        for line in taulukko:
            if line:
                rivi = re.match(r'\s*(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(\w+[ ]?\w*)',line)
                tulos = rivi.groups()
                result.append('\t'.join(tulos))

    return result


def main():
    print(red_green_blue("rgb.txt"))

if __name__ == "__main__":
    main()
