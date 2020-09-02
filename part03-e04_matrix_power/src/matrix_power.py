#!/usr/bin/env python3
import numpy as np
import functools

def matrix_power(a, n):
#    print(a)
    if n==0:
        a[:] = np.eye(a.shape[0])
    elif n>0:
        a = functools.reduce(lambda x,y:x@y,[a for i in range(n)])
    elif n<0:
        a=np.linalg.inv(a)
        a = functools.reduce(lambda x,y:x@y,[a for i in range(0-n)])
    a= np.array(a)
    return a
#    print(a)
def main():
    matrix_power(np.array([[1, 2], [3, 4]]),1)
    matrix_power(np.array([[1,2,3],[4,5,6],[7,8,9]]),0)
    matrix_power(np.array([[1,2,3],[4,5,6],[7,8,9]]),-2)
    return

if __name__ == "__main__":
    main()
