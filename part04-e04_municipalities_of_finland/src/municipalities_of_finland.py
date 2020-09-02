#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    stat = pd.read_csv('src/municipal.tsv',sep='\t',index_col='Region 2018')
    result = stat.loc['Akaa':'Äänekoski']
    return result
    
def main():
    print(municipalities_of_finland())
    return
    
if __name__ == "__main__":
    main()
