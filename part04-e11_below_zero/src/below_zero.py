#!/usr/bin/env python3

import pandas as pd

def below_zero():
    stat = pd.read_csv('src/kumpula-weather-2017.csv')
    m=stat['Air temperature (degC)']<0
    result = stat[m]
    res=result['m'].count()
    return res
  

def main():
    print(f'Number of days below zero: {below_zero()}')
    return
    
if __name__ == "__main__":
    main()
