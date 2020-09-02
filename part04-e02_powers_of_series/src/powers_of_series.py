#!/usr/bin/env python3

import pandas as pd
import math

def powers_of_series(s, k):
    s1=s
    for i in range (k-1):
        s1=pd.concat([s1,pow(s,i+2)],axis=1)
    df=pd.DataFrame(s1)
    df.columns=[item for item in range(1,k+1)]
    return df
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 5))
    return
    
if __name__ == "__main__":
    main()
