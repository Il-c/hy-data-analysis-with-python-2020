#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math

def center(a):
    y, x = a.shape[:2]
    y=(y-1)/2
    x=(x-1)/2
    return (y,x)   # note the order: (center_y, center_x)

def radial_distance(a):
    result = np.zeros((a.shape[0],a.shape[1]))
    y,x = center(a)
    i=0
    for row in result:
        j=0
        for cell in row:
            result[i,j] = math.sqrt((i-y)*(i-y)+(j-x)*(j-x))
            j +=1
        i+=1
    return result

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    b = np.interp(a,(a.min(),a.max()),(tmin,tmax))
    return b

def radial_mask(a):
    b=radial_distance(a)
    if b.shape[0]>2:
            return 1-scale(b)   
    if b.shape[1]>2:
            return 1-scale(b)
    return scale(b)

def radial_fade(a):
    height, width = a.shape[:2]
    m=radial_mask(a).reshape(height,width,1)
    return a*m

def main():
 
    painting = plt.imread("painting.png")
    new_painting = painting.copy()
    plt.subplot(3,1,1)
    plt.imshow(painting)
    plt.subplot(3,1,2)
    plt.imshow(radial_mask(new_painting))
    plt.subplot(3,1,3)
    plt.imshow(radial_fade(new_painting))
    plt.show()
 

if __name__ == "__main__":
    main()
