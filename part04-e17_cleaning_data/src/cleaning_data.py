#!/usr/bin/env python3

import pandas as pd
import numpy as np
from string import ascii_letters


def cleaning_data():
    data = pd.read_csv('src/presidents.tsv',sep='\t')
    data.Start = data.Start.str.strip(ascii_letters)
    data.Start = data.Start.str.strip()

    filter = data.Seasons.str.isalpha()
    data.Seasons[filter]=data.Seasons[filter].map({'one':1,'two':2})
   
    data.President=data.President.apply(lambda x: x.split(',')[::-1])
    data.President=data.President.apply(lambda x: ','.join(x))
    data.President=data.President.str.lstrip()
    data.President=data.President.str.replace(',',' ')

    data['Vice-president']=data['Vice-president'].apply(lambda x: x.split(',')[::-1])
    data['Vice-president']=data['Vice-president'].apply(lambda x: ','.join(x))
    data['Vice-president']=data['Vice-president'].str.replace(',',' ')
    data['Vice-president']=data['Vice-president'].str.lstrip()
    data['Vice-president']=data['Vice-president'].str.title()

    data['Last']=pd.to_numeric(data['Last'],errors='coerce')
    data = data.astype({"President": object, "Start": int, "Seasons": int, "Vice-president": object})

    return data

def main():
    print(cleaning_data().dtypes)
    return

if __name__ == "__main__":
    main()
