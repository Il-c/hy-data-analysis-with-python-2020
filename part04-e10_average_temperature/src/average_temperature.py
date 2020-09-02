#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    stat = pd.read_csv('src/kumpula-weather-2017.csv')
    m=stat['m']==7
    result = stat[m]
    res=result['Air temperature (degC)'].mean()
    return res
  

def main():
    print(f'Average temperature in July: {average_temperature():.1f}')
    return

if __name__ == "__main__":
    main()
