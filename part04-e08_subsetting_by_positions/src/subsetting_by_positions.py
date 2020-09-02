#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    stat = pd.read_csv('src/UK-top40-1964-1-2.tsv',sep='\t')
    result = stat.iloc[1:11,[2,3]]
    return result

def main():
    print(subsetting_by_positions())
    return

if __name__ == "__main__":
    main()
