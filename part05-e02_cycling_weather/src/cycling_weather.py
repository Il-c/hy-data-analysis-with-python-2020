#!/usr/bin/env python3

import pandas as pd


def cycling_weather():
    weather_data=pd.read_csv('src/kumpula-weather-2017.csv')
    cyclist_data=split_date_continues()
    result = pd.merge(cyclist_data,weather_data, right_on=['d','m','Year'],left_on=['Day','Month','Year'])
    result = result.drop(columns=['m','d','Time','Time zone'])

    return result

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
    

def main():
    print(cycling_weather().head)
    return

if __name__ == "__main__":
    main()
