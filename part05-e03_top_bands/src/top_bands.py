#!/usr/bin/env python3

import pandas as pd

def top_bands():
    top40 = pd.read_csv('src/UK-top40-1964-1-2.tsv',sep='\t')
    top_bands=pd.read_csv('src/bands.tsv',sep='\t')
    top_bands.Band=top_bands.Band.str.upper()
  #  print(top_bands)
    result = pd.merge(top40, top_bands,left_on=['Artist'], right_on='Band' )
  #  result = result.drop(columns='Band')
    return result

def main():
    print(top_bands())
    return

if __name__ == "__main__":
    main()
