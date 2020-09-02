#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def mystery_data():
    data = pd.read_csv('src/mystery_data.tsv',sep='\t')
    model=LinearRegression(fit_intercept=False)
    model.fit(np.vstack([data.X1,data.X2,data.X3,data.X4,data.X5]).T, data.Y)
    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    print(f'Coefficient of X1 is {coefficients[0]}\n\
Coefficient of X2 is {coefficients[1]}\n\
Coefficient of X3 is {coefficients[2]}\n\
Coefficient of X4 is {coefficients[3]}\n\
Coefficient of X5 is {coefficients[4]}\n')
    
if __name__ == "__main__":
    main()
