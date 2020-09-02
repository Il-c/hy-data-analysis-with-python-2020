#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    result=[]
    i = 0
    while i<a.shape[0]:
        result.extend(a[i,np.newaxis])
        i+=1
    return result

def get_columns(a):
    result=[]
    a=a.T
    result = [row for row in a]
        
    return result
    

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
