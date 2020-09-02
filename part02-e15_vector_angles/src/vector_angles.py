#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    n = (X*Y).sum(axis=1)
    a = scipy.linalg.norm(X, 2, axis=1)
    b = scipy.linalg.norm(X, 2, axis=1)
    d = a*b
    temp = n/d
    result = np.degrees(np.arccos(np.clip(temp,0,1)))
    return result

def main():
    print(vector_angles(np.array([[0,0,1],
 [-1,1,0]]),np.array([[0,1,0],
 [1,1,0]])))
    np.array([])

if __name__ == "__main__":
    main()
