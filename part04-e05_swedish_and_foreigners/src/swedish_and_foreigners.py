#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    stat = pd.read_csv('src/municipal.tsv',sep='\t',index_col='Region 2018')
    result = stat.loc['Akaa':'Äänekoski']
    result = result.loc[(result['Share of Swedish-speakers of the population, %']>5) & (result['Share of foreign citizens of the population, %']>5)]
    result = result.iloc[:,[0,2,3]]
    return result
    
def main():
    print(swedish_and_foreigners())
    return

if __name__ == "__main__":
    main()
