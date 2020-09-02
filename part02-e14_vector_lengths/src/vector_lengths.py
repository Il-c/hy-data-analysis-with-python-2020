#!/usr/bin/env python3
import math
import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a = (np.sqrt((a**2).sum(axis=1)))
    return a


def main():
    print(vector_lengths(np.array([[1,2,3],[4,5,6]])))

if __name__ == "__main__":
    main()
