#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def coefficient_of_determination():
    score = np.array([0.0,0.0,0.0,0.0,0.0,0.0])
    data = pd.read_csv('src/mystery_data.tsv',sep='\t')
    model=LinearRegression(fit_intercept=True)
    model.fit(data.loc[:,'X1':'X5'], data.Y)
    score[0] =model.score(data.loc[:,'X1':'X5'],data.Y)
    for i in range(5):
        model.fit(data.iloc[:,i].values.reshape(-1,1), data.Y)
        score[i+1]=model.score(data.iloc[:,i].values.reshape(-1,1),data.Y)
    return score
def main():
    score = coefficient_of_determination()
    for i, j in enumerate (score):
        print(f'R2-score with feature(s) X{i}: {j}')
    
if __name__ == "__main__":
    main()
