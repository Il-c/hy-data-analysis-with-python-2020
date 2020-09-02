#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        elif shape == "triangle":
            areaOfTriangle()
        elif shape == "rectangle":
            areaOfRectangle()
        elif shape == "circle":
            areaOfCircle()
        else:
            print("Unknown shape!")

def areaOfTriangle():
    base = input("Give base of the triangle:")
    height = input("Give height of the triangle:")
    area = int(base)*int(height)/2
    print(f"The area is {area:09.6f}")
    
def areaOfRectangle():
    base = input("Give width of the rectangle:")
    height = input("Give height of the rectangle:")
    area = int(base)*int(height)
    print(f"The area is {area:09.6f}")
def areaOfCircle():
    radius = input("Give radius of the circle:")
    area = int(radius)**2*math.pi
    print(f"The area is {area:09.6f}")
    

if __name__ == "__main__":
    main()
