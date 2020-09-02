#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    stat=pd.read_csv('src/UK-top40-1964-1-2.tsv',sep='\t')
    stat['LW']=pd.to_numeric(stat['LW'],errors='coerce')
    m = (stat['LW']<stat['Pos'])
    res = stat[m]
    res['LW']=res['LW'].map(int)

    return res

def main():
    print(special_missing_values())
    return

if __name__ == "__main__":
    main()
