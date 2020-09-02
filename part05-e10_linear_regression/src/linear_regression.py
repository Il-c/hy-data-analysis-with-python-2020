#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model=LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis], y)
    return (model.coef_[0],model.intercept_)
    
def main():
    x=np.array([2,3,4,5])
    y=np.array([5,6,3,2])
    slope,intercept=fit_line(x,y)
    print(f'Slope: {slope}\nIntercept: {intercept}')
    xfit=np.linspace(0,10,100)
    yfit=xfit*slope + intercept
    plt.plot(xfit,yfit, color="black")
    plt.plot(x,y, 'o')
    plt.show()
    
if __name__ == "__main__":
    main()
