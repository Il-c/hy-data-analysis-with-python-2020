#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    df=pd.DataFrame([[np.nan,None],[1917,'Niinistö'],[1776,'Trump'],[1523,None],[np.nan,'Steinmeier'],[1992,'Putin']],columns=['Year of independence','President'],index=["United Kingdom","Finland","USA","Sweden","Germany",'Russia'])#,dtype='float')
    df=df.rename_axis(columns='State')
    return df
   
               
def main():
    print(missing_value_types())
    return

if __name__ == "__main__":
    main()
