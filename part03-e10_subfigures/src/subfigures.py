#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
 #   fig, ax = plt.subplots(1,2)
    plt.subplot(1,2,1)
    plt.plot(a[:,0],a[:,1])
    plt.subplot(1,2,2)
    plt.scatter(a[:,0],a[:,1],c=a[:,2],s=a[:,3])
    plt.show()


def main():
    subfigures(np.array([[1,2,5,6],[5,2,7,5],[6,7,2,3],[3,4,1,3]]))

if __name__ == "__main__":
    main()
