#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def split_date(data):
    data=data['Päivämäärä'].str.split(expand=True)
    data.columns=['Weekday','Day','Month','Year','Hour']

    data.Month = data.Month.map({'tammi':1,'helmi':2,'maalis':3,'huhti':4,'touko':5,'kesä':6,'heinä':7,'elo':8,'syys':9,'loka':10,'marras':11,'joulu':12})
    data.Weekday = data.Weekday.map({'ma':'Mon','ti':'Tue','ke':'Wed','to':'Thu','pe':'Fri','la':'Sat','su':'Sun'})
    data.Hour = data.Hour.str.split(':',expand=True)
    data = data.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return data

def split_date_continues():
    data = pd.read_csv('src/Helsingin_pyorailijamaarat.csv',sep=';')
    data=data.dropna(how='all')
    data=data.dropna(axis=1,how='all')
    split_data=split_date(data)
    result=pd.concat([split_data,data],axis=1)
    result=result.drop(columns=['Päivämäärä'],axis=1)
    return result


def bicycle_timeseries():
    data = split_date_continues()
    data['Päivämäärä']=pd.to_datetime(data[['Year','Month','Day','Hour']])
    data = data.set_index('Päivämäärä')
    data = data.drop(columns=['Year','Month','Day','Hour'],axis=1)
    return data

def commute():
    data = bicycle_timeseries()
    data.Weekday = data.Weekday.map({'Mon':1,'Tue':2,'Wed':3,'Thu':4,'Fri':5,'Sat':6,'Sun':7})
    data = data['2017-08-01':'2017-08-31']
    grouped = data.groupby(['Weekday']).sum()
    data = data.set_index('Weekday')
    return grouped
    
def main():
    data=commute()
    plt.plot(data)
    plt.show()
    return


if __name__ == "__main__":
    main()
