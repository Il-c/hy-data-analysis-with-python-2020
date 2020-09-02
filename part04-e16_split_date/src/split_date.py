#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    data = pd.read_csv('src/Helsingin_pyorailijamaarat.csv',sep=';')
    data=data.dropna(how='all')
    data=data.dropna(axis=1,how='all')
    data=data['Päivämäärä'].str.split(expand=True)
    data.columns=['Weekday','Day','Month','Year','Hour']

    data.Month = data.Month.map({'tammi':1,'helmi':2,'maalis':3,'huhti':4,'touko':5,'kesä':6,'heinä':7,'elo':8,'syys':9,'loka':10,'marras':11,'joulu':12})
    data.Day = data.Day.astype(int)
    data.Year = data.Year.astype(int)
    data.Weekday = data.Weekday.map({'ma':'Mon','ti':'Tue','ke':'Wed','to':'Thu','pe':'Fri','la':'Sat','su':'Sun'})
    data.Hour = data.Hour.str.split(':',expand=True)
    data.Hour = data.Hour.astype(int)
    return data

def main():
    print(split_date())
    print(split_date().dtypes)
    return
       
if __name__ == "__main__":
    main()
