#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    array = load()
    sep_len = array[:,0]
    pet_len = array[:,2]
    res = scipy.stats.pearsonr(sep_len,pet_len)
    return res[0]

def correlations():
    array = load()
    new_array=array[:,:4]
    res = np.corrcoef(array,None,False)
    return res

def main():
    
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
