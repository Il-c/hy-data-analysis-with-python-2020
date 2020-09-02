#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    stat = pd.read_csv('src/UK-top40-1964-1-2.tsv',sep='\t')
    stat['LW']=pd.to_numeric(stat['LW'],errors='coerce')
  

    m=stat['LW'].isnull()
    stat[m]=np.nan

    m=(stat['Peak Pos']==stat['Pos'])&(stat['Peak Pos']<stat['LW'])
    stat['Peak Pos'][m]=np.nan
    
    stat['Pos']=np.nan
    stat=stat.reindex(columns=['LW','Pos','Title','Artist','Publisher','Peak Pos','WoC'])
    stat =stat.rename({'LW':'Pos','Pos':'LW'},axis=1)
 
    lst = (stat['Pos'].values)
    lst=[x for x in range(1,41) if x not in lst]
    stat=stat.dropna(how='all')
 
    

    df = pd.DataFrame({'Pos':lst,'LW':np.nan,'Title':np.nan,'Artist':np.nan,'Publisher':np.nan,'Peak Pos':np.nan,'WoC':np.nan})
    stat=stat.append(df)
    stat['WoC']=stat['WoC']-1
    
 
    stat = stat.reset_index(drop=True)

  
    stat=stat.sort_values(by=['Pos'])
    stat['Pos']=stat['Pos'].astype(int)
    return stat

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
