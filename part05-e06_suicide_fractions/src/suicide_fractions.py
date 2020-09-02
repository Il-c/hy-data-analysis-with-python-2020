#!/usr/bin/env python3
import numpy as np
import pandas as pd

def suicide_fractions():
    top40 = pd.read_csv('src/who_suicide_statistics.csv',sep=',')
    top40=top40.dropna(subset=['suicides_no'])
    top40['suicides_no']=top40.suicides_no/top40.population
    tulos=top40.groupby('country').mean()
    group=tulos.suicides_no
    return group

def main():
    print(suicide_fractions())
    return

if __name__ == "__main__":
    main()
