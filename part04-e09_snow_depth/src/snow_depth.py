#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    stat = pd.read_csv('src/kumpula-weather-2017.csv')
    result = stat['Snow depth (cm)'].max()
    return result

def main():
    print(f'Max snow depth: {snow_depth():.1f}')
    return

if __name__ == "__main__":
    main()
