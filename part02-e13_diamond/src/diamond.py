#!/usr/bin/env python3

import numpy as np

def diamond(n):

    first = np.eye(n, dtype=int)
    half = first[::-1,:]
    upperhalf = np.concatenate((half,first[:,1:(n)]), axis = 1)
    lowerhalf = np.concatenate((first,half[:,1:n]), axis = 1)
    result = np.concatenate((upperhalf,lowerhalf[1:n,:]))
    return result
  #  return np.array([])

def main():
    print(diamond(1))

if __name__ == "__main__":
    main()
