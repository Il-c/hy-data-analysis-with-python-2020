#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt



def to_grayscale(painting):
    new_painting = painting.copy()
    rgb_weights = [0.2126,0.7152,0.0722]
    new_painting=np.dot(new_painting[...,:3], rgb_weights)
 #print(new_painting.shape)
    return new_painting

def to_red(painting):
    new_painting = painting.copy()
    new_painting[:,:,1]=new_painting[:,:,1]*0
    new_painting[:,:,2]=new_painting[:,:,2]*0
 
    return new_painting
def to_green(painting):
    new_painting = painting.copy()
    new_painting[:,:,0]=new_painting[:,:,0]*0
    new_painting[:,:,2]=new_painting[:,:,2]*0
 
    return new_painting
def to_blue(painting):
    new_painting = painting.copy()
    new_painting[:,:,0]=new_painting[:,:,0]*0
    new_painting[:,:,1]=new_painting[:,:,1]*0

    return new_painting



def main():
    painting = plt.imread("src/painting.png")
    plt.subplot(3,1,1)
    plt.imshow(to_red(painting))
    plt.subplot(3,1,2)
    plt.imshow(to_green(painting))
    plt.subplot(3,1,3)
    plt.imshow(to_blue(painting))

   # plt.imshow(to_grayscale(painting))
    plt.show()
    

if __name__ == "__main__":
    main()
