#!/usr/bin/env python3

import pandas as pd

def cyclists():
    stat = pd.read_csv('src/Helsingin_pyorailijamaarat.csv',sep=';')
    stat=stat.dropna(how='all')
    stat=stat.dropna(axis=1,how='all')
    return stat


def main():
    print((cyclists()).shape)
    return
    
if __name__ == "__main__":
    main()
