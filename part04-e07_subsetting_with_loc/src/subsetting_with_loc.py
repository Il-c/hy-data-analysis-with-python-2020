#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    stat = pd.read_csv('src/municipal.tsv',sep='\t',index_col='Region 2018')
    result = (stat.loc['Akaa':'Äänekoski']).loc[:,["Population", "Share of Swedish-speakers of the population, %","Share of foreign citizens of the population, %"]]
    return result

def main():
    print(subsetting_with_loc())
    return

if __name__ == "__main__":
    main()
