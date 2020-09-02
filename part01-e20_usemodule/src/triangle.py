"This module has functions to calculate right-angled triangle's hypotenuse and area"
__version__ = "1.0"
__author__ = "Ilari Lehtinen"
# Enter you module contents here
import math
def hypothenuse(x,y):
    "This function calculates hypotenuse of right-angled triangle"
    hypothenuse = math.sqrt(x**2+y**2)
    return hypothenuse
def area(x,y):
    "This function calculates area of right-angled triangle"
    area = (x*y)/2
    return area