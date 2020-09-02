#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def read_series():
    s=pd.Series(dtype='object')
    while True:
        input1 = input("Give index and value separated by whitespace: ")
        if input1 == '':
            break
        if input1 != '' and (len(input1.split()))!=2:
            raise Exception("Invalid entry!")
        s[input1.split()[0]]=input1.split()[1]
    return s

def main():
    print(read_series())

if __name__ == "__main__":
    main()
