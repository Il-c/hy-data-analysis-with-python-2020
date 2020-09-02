#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    m2 = a.shape[1]
    m = int(m2/2)
    c = (np.sum(a[:,:m],axis=1))>(np.sum(a[:,-m:],axis=1))
    result = a[c]
    return result
    

def main():
    print(first_half_second_half(np.array([[1,3,4,2],[2,2,1,2]])))

if __name__ == "__main__":
    main()
