#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):

    m = (df['Population change from the previous year, %']>0)
    result = df[m]
    prop = result.shape[0]/df.shape[0]
    return prop

def main():
    stat = pd.read_csv('src/municipal.tsv',sep='\t',index_col='Region 2018')
    result = stat.loc['Akaa':'Äänekoski']
    prop = growing_municipalities(result)*100
    print(f'Proportion of growing municipalities: {prop:.1f}%')
    return

if __name__ == "__main__":
    main()
