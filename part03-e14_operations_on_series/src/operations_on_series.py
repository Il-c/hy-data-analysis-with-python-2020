#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    s1 = pd.Series(L1, index=['a','b','c'])
    s2 = pd.Series(L2, index=['a','b','c'])
    return (s1, s2)
    
def modify_series(s1, s2):
    s1.add(s2['b'])
    s1['d']=s2['b']
    s3=s2.drop('b')
    return (s1, s3)
    
def main():
    L1 = [2,4,6]
    L2 = [3,5,6]
    s1, s2 = create_series(L1, L2)
    print(s1, ' ja \n',s2)
    s1, s2 = modify_series(s1,s2)
    s3 = s1.add(s2)
    print('Modified:\n ',s1, ' ja \n',s2,'jaaa',s3)
    return
    
if __name__ == "__main__":
    main()
