#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    top40 = pd.read_csv('src/UK-top40-1964-1-2.tsv',sep='\t')
    group=top40.groupby('Publisher').WoC.sum().reset_index()
    group=group.sort_values('WoC',ascending=False)
    result=top40[top40['Publisher']==group.iloc[0,0]]

    return result

def main():
    best_record_company()
    return
    

if __name__ == "__main__":
    main()
