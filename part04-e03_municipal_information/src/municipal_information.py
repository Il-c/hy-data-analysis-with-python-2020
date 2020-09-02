#!/usr/bin/env python3

import pandas as pd

def main():
    stat = pd.read_csv('src/municipal.tsv',sep='\t')
    print('Shape:',(str(stat.shape[0]))+',',stat.shape[1])
    print("Columns:")
    [print(column) for column in stat.columns]
    return


if __name__ == "__main__":
    main()
